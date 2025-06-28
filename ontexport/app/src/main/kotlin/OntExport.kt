import java.io.File
import java.nio.file.Files
import java.security.MessageDigest

import org.semanticweb.owlapi.apibinding.OWLManager
import org.semanticweb.owlapi.formats.*
import org.semanticweb.owlapi.model.*
import org.semanticweb.owlapi.reasoner.*
import org.semanticweb.owlapi.util.*
import org.semanticweb.owlapi.io.FileDocumentSource
import org.semanticweb.HermiT.Reasoner

import org.slf4j.LoggerFactory

fun main(args: Array<String>) {
    val logger = LoggerFactory.getLogger("OntExport")

    if (args.size < 1) {
        logger.error("Missing arguments <input-folder> [--abox <abox1.ttl> <abox2.ttl> ...]")
        return
    }

    val config = OWLOntologyLoaderConfiguration().apply {
        isLoadAnnotationAxioms = true
        isFollowRedirects = false
    }

    val path = File(args[0])
    val aBoxIndex = args.indexOf("--abox")
    val aBoxList = if (aBoxIndex != -1) {
        args.drop(aBoxIndex + 1).toSet()
    } else emptySet()

    val files = path.listFiles { _, name ->
        name.endsWith(".ttl") && !name.endsWith("-inferred.ttl")
    }?.toList() ?: emptyList()

    val formats = listOf(
        RDFXMLDocumentFormat(),
        RDFJsonLDDocumentFormat()
    )

    val manager = OWLManager.createOWLOntologyManager()

    // Map local ontologies
    files.forEach { file ->
        parseTurtleFile(file)?.let { iri ->
            manager.getIRIMappers().add(SimpleIRIMapper(iri, IRI.create(file)))
        }
    }

    // Write ontology only if changed
    fun writeIfChanged(
        ont: OWLOntology,
        output: File,
        ext: String,
        format: OWLDocumentFormat
    ) {
        val temp = Files.createTempFile("temp", ".$ext").toFile()
        manager.saveOntology(ont, format, temp.outputStream())

        if (!output.exists()) {
            temp.copyTo(output)
            logger.info("Created ${output.name}")
        } else if (!filesAreEqual(temp, output)) {
            temp.copyTo(output, overwrite = true)
            logger.info("Updated ${output.name}")
        }

        temp.delete()
    }

    // 1. Convert all .ttl files except those in aBoxList
    files.filterNot { aBoxList.contains(it.name) }.forEach { file ->

        val ont = manager.loadOntologyFromOntologyDocument(FileDocumentSource(file), config)

        formats.forEach { format ->
            val ext = when (format) {
                is RDFXMLDocumentFormat -> "owl"
                is RDFJsonLDDocumentFormat -> "jsonld"
                else -> "out"
            }
            val output = File(file.parentFile, "${file.nameWithoutExtension}.$ext")
            writeIfChanged(ont, output, ext, format)
        }

        // Update source ontology
        val turtle = TurtleDocumentFormat()
        manager.getOntologyFormat(ont)?.let {
            turtle.copyPrefixesFrom(it.asPrefixOWLDocumentFormat().getPrefixName2PrefixMap())
        }

        writeIfChanged(ont, file, "ttl", turtle)
        manager.removeOntology(ont)
    }

    val reasonerFactory = Reasoner.ReasonerFactory()

    // 2. Reasoning over each ABox
    aBoxList.forEach { name ->
        val file = File(path, name)
        val ont = manager.loadOntologyFromOntologyDocument(FileDocumentSource(file), config)

        val reasoner = reasonerFactory.createReasoner(ont);
        reasoner.precomputeInferences()

        val generators: List<InferredAxiomGenerator<out OWLAxiom>> = listOf(
            InferredClassAssertionAxiomGenerator(),
            InferredDataPropertyCharacteristicAxiomGenerator(),
            // InferredDisjointClassesAxiomGenerator(),
            InferredEquivalentClassAxiomGenerator(),
            InferredEquivalentDataPropertiesAxiomGenerator(),
            InferredEquivalentObjectPropertyAxiomGenerator(),
            InferredInverseObjectPropertiesAxiomGenerator(),
            InferredObjectPropertyCharacteristicAxiomGenerator(),
            InferredPropertyAssertionGenerator(),
            InferredSubClassAxiomGenerator(),
            InferredSubDataPropertyAxiomGenerator(),
            InferredSubObjectPropertyAxiomGenerator()
        )

        val iri = ont.ontologyID.ontologyIRI
            .orElseThrow { IllegalArgumentException("Ontology ${file.name} has no IRI") }

        val infIri = IRI.create(iri.toString() + "-inferred")
        val infOnt = manager.createOntology(infIri)

        manager.addAxioms(infOnt, ont.axioms)
        val generator = InferredOntologyGenerator(reasoner, generators)
        generator.fillOntology(manager.owlDataFactory, infOnt)

        val infOut = File(path, "${file.nameWithoutExtension}-inferred.ttl")

        // Update source and inferred ontologies
        val turtle = TurtleDocumentFormat()
        manager.getOntologyFormat(ont)?.let {
            turtle.copyPrefixesFrom(it.asPrefixOWLDocumentFormat().getPrefixName2PrefixMap())
        }

        writeIfChanged(ont, file, "ttl", turtle)
        writeIfChanged(infOnt, infOut, "ttl", turtle)

        manager.removeOntology(ont)
    }
}

fun parseTurtleFile(file: File): IRI? {
    val pattern = Regex("""<([^>]+)>\s+(a|rdf:type)\s+owl:Ontology""")
    file.useLines { lines ->
        for (line in lines) {
            val trimmed = line.trim()
            if ("owl:Ontology" in trimmed) {
                val match = pattern.find(trimmed)
                if (match != null) {
                    val iri = match.groupValues[1]
                    return IRI.create(iri)
                }
            }
        }
    }
    return null
}

fun filesAreEqual(file1: File, file2: File): Boolean {
    val digest = MessageDigest.getInstance("SHA-256")
    val hash1 = digest.digest(file1.readBytes())
    val hash2 = digest.digest(file2.readBytes())
    return hash1 contentEquals hash2
}
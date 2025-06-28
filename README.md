# CONTRO: A Controversy-Oriented Model of Dialectical Perspectives

**CONTRO** is an ontology for extracting dialectical perspectives from argumentative discourse. It was developed as the final project for the [*Knowledge Representation and Knowledge Extraction* course](https://www.unibo.it/en/study/course-units-transferable-skills-moocs/course-unit-catalogue/course-unit/2023/490896) (2023–2024) at the University of Bologna, part of the Master’s in Digital Humanities and Digital Knowledge.

## Vision

CONTRO models how opinions emerge through opposition, reconstructing arguments from minimal annotations of premises and conclusions. Its goal is to **bridge structured argumentation and perspective modeling**, enabling OWL reasoners to infer conflicting viewpoints from discursive evidence.

## Ontological Approach

CONTRO combines two paradigms:

- The **ASPIC+ framework**, to model the internal structure of arguments and their interactions.
- The **perspectivisation ontology design pattern**, to reframe argumentation as a conceptualiser’s construal of a situation.

It builds on the **Descriptions and Situations (DnS)** module of DOLCE, treating ontology classes not as definitions of what an instance *is*, but of what it can be *described as*. This ensures principled conceptual commitments that support domain-agnostic modeling.

## Reference Scenario

To develop and test the ontology, we annotated a major Renaissance controversy between Annibal Caro and Lodovico Castelvetro over Petrarchism. TEI markup and manual extraction of arguments from their treatises helped expose both the potential and limitations of the model.

## Documentation Pipeline

This site is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and treats ontologies as source code: extraction, reasoning, serialization, and documentation are integrated into a reproducible build process.

The pipeline includes:

1. **TEI to Markdown**  
   [`tei-to-markdown.py`](scripts/tei-to-markdown.py) converts TEI files via a custom [XSLT stylesheet](tei/stylesheets/tei-to-markdown-custom.xsl), generating Markdown with embedded argument outlines for interactive reading.

2. **TEI to RDF**  
   [`tei-to-turtle.py`](scripts/tei-to-turtle.py) extracts argument instances into [data.ttl](docs/ont/data.ttl), aligning them with the ontology.

3. **Ontology Export and Reasoning**  
   [`OntExport.kt`](ontexport/app/src/main/kotlin/OntExport.kt) serializes the TBox in TTL, RDF/XML, and JSON-LD formats, and runs HermiT over the ABoxes (`example.ttl`, `data.ttl`) to output inferred ontologies. It is compiled as a standalone [JAR](ontexport/app/build/libs/ontexport.jar) with no Java runtime dependencies.

4. **Ontology Documentation**  
   The [`ontdoc`](scripts/ontdoc/) module maps ontology elements to Python objects and handles their representation: it resolves punning, links terms across submodules, and additionally documents the extension of imported classes and properties. A Jinja2 [template](templates/doc-template.md) then generates Markdown descriptions for each submodule.

## Machine Accessibility

All ontology terms are dereferenceable through a custom [`.htaccess`](https://github.com/cccontro/w3id.org/blob/master/contro/.htaccess) setup registered with w3id.org, ensuring long-term stable URIs for both human and machine consumption.

## Contributors

- [Francesca Massarenti](https://github.com/frammenti) - francesca.massarent2@studio.unibo.it
- [Alberto Ciarrocca](https://github.com/vattelalberto) - alberto.ciarrocca@studio.unibo.it

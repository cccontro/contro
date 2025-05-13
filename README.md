# CONTRO: A Controversy-Oriented Model of Dialectical Perspectives
The **CONTRO ontology** was developed as a final project for the [*Knowledge Representation and Knowledge Extraction* course](https://www.unibo.it/en/study/course-units-transferable-skills-moocs/course-unit-catalogue/course-unit/2023/490896), taught by Professor Aldo Gangemi during the 2023/2024 academic year at the University of Bologna. The course was part of the Master's program in Digital Humanities and Digital Knowledge.

## The ontology
CONTRO is designed to extract both explicit and implicit opinions as they emerge through dialectical discourse. Its focus is on reconstructing argumentative structures in text from minimal annotation of premises and conclusions, leveraging the inferential power of OWL reasoners.

The ontology integrates two core approaches:

- It adopts the **ASPIC<sup>+</sup> framework**, a widely used formalism for structured argumentation, to model the internal components of argumentation within discourse.
- It then reinterprets these elements through the **perspectivization ontology design pattern**, which allows for a synchronic representation of argumentative positions, flattening their diachronic development into coexisting perspectives.

CONTRO adopts the **Descriptions and Situations (DnS)** model from the DOLCE foundational ontology. This choice supports domain-agnostic modeling, treating argumentative roles and structures as context-dependent descriptions instantiated by discourse situations.  As a result, CONTRO can be applied independently of any specific domain conceptualization, making it adaptable to a wide range of argumentative genres and subject matters.

## About this documentation
This website is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), customized for ontology documentation through a combination of plugins, CSS, and JavaScript. We treat the ontology as a programming module, and believe that tight integration between documentation and ontology is essential for the kind of reuse the Semantic Web is meant to foster.

To support this vision, we developed a build [pipeline](hook.py) that automates several tasks: extracting ontology instances from the source text ([`conversion.py`](https://github.com/cccontro/contro/blob/main/docs/ont/conversion.py)), generating element descriptions via integration with [Widoco](https://github.com/dgarijo/Widoco), and converting the XML-TEI source file to Markdown ([`transformation.py`](https://github.com/cccontro/contro/blob/main/docs/tei/transformation.py)). All outputs are incorporated into the site with a consistent presentation.

While ensuring a coherent human-readable documentation, we also preserved machine accessibility for ontology elements, using a custom [`.htaccess`](https://github.com/cccontro/w3id.org/blob/ee15a85c1808daf4680f02fe1437d4882c0380f7/contro/.htaccess) redirection protocol that supports Semantic Web resolution practices.

## Contributors
- [Francesca Massarenti](https://github.com/frammenti) - francesca.massarent2@studio.unibo.it
- [Alberto Ciarrocca](https://github.com/vattelalberto) - alberto.ciarrocca@studio.unibo.it

<!--- This file was automatically generated - do not edit -->

<h1>Controversy Ontology <small>(contro)</small></h1>

## Overview

**IRI:** <https://w3id.org/contro>

**Version:** 0.7

**Release:** 12/03/2025

**Last update:** 17/06/2025

**Authors:** Alberto Ciarrocca, Francesca Massarenti

**License:** [![License: CC BY 4.0](https://img.shields.io/badge/-CC%20BY%204.0-lightgrey.svg?style=for-the-badge)](https://creativecommons.org/licenses/by/4.0/)

**Available:**

[![Format: TTL](https://img.shields.io/badge/Format-TTL-green.svg?style=for-the-badge)](https://w3id.org/contro.ttl)
[![Format: XML/RDF](https://img.shields.io/badge/Format-XML/RDF-red.svg?style=for-the-badge)](https://w3id.org/contro.owl)
[![Format: JSON-LD](https://img.shields.io/badge/Format-JSON--LD-blue.svg?style=for-the-badge)](https://w3id.org/contro.jsonld)

### Description
An ontology for extracting perspectives from arguments. It builds on the ASPIC+ framework to formalize arguments and maps them to perspectives on the topic under discussion. The mapping is implemented via object property subclassing, preserving the conceptual separation between the argument structure and the perspectival interpretation.


### Imported Ontologies
<https://w3id.org/contro/arg>

<https://w3id.org/contro/persp>


### Namespaces

| Prefix | URI |
|--------|-----------|
| arg | <https://w3id.org/contro/arg#> |
| dc | <http://purl.org/dc/elements/1.1/> |
| dct | <http://purl.org/dc/terms/> |
| owl | <http://www.w3.org/2002/07/owl#> |
| persp | <https://w3id.org/contro/persp#> |
| rdf | <http://www.w3.org/1999/02/22-rdf-syntax-ns#> |
| rdfs | <http://www.w3.org/2000/01/rdf-schema#> |
| vann | <http://purl.org/vocab/vann/> |


## Object Properties

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="ersp/#Background_op">Background</h3>
      <a class="object_property" href="persp/#Background_op">https://w3id.org/contro/persp#Background</a>
    </div>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        <a class="object_property" href="arg/#ArgumentationTheory_op" title="https://w3id.org/contro/arg#ArgumentationTheory">Argumentation Theory</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="arg/#KnowledgeBase_op" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="rg/#by_op">by</h3>
      <a class="object_property" href="arg/#by_op">https://w3id.org/contro/arg#by</a>
    </div>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="persp/#Conceptualiser_op" title="https://w3id.org/contro/persp#Conceptualiser">Conceptualiser</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="rg/#Conclusion_op">Conclusion</h3>
      <a class="object_property" href="arg/#Conclusion_op">https://w3id.org/contro/arg#Conclusion</a>
    </div>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="persp/#Cut_op" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="ersp/#contrasts_op">contrasts</h3>
      <a class="object_property" href="persp/#contrasts_op">https://w3id.org/contro/persp#contrasts</a>
    </div>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        inverse(<a class="object_property" href="persp/#Cut_op" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="op" title="Object Property"></span>) o <a class="object_property" href="arg/#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="arg/#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="arg/#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span>) o <a class="object_property" href="persp/#Cut_op" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="rg/#Premise_op">Premise</h3>
      <a class="object_property" href="arg/#Premise_op">https://w3id.org/contro/arg#Premise</a>
    </div>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="persp/#Lens_op" title="https://w3id.org/contro/persp#Lens">Lens</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="rg/#Topic_op">Topic</h3>
      <a class="object_property" href="arg/#Topic_op">https://w3id.org/contro/arg#Topic</a>
    </div>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="persp/#Eventuality_op" title="https://w3id.org/contro/persp#Eventuality">Eventuality</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>






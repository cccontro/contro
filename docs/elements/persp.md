<!--- This file was automatically generated - do not edit -->

<h1>Perspectivisation Ontology <small>(persp)</small></h1>

## Overview

**IRI:** <https://w3id.org/contro/persp>

**Version:** 1.0

**Release:** 12/03/2025

**Last update:** 21/05/2025

**Authors:** Alberto Ciarrocca, Francesca Massarenti

**Source:** <http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl>

**License:** [![License: CC BY 4.0](https://img.shields.io/badge/-CC%20BY%204.0-lightgrey.svg?style=for-the-badge)](https://creativecommons.org/licenses/by/4.0/)

**Available:**

[![Format: TTL](https://img.shields.io/badge/Format-TTL-green.svg?style=for-the-badge)](https://w3id.org/contro/persp.ttl)
[![Format: XML/RDF](https://img.shields.io/badge/Format-XML/RDF-red.svg?style=for-the-badge)](https://w3id.org/contro/persp.owl)
[![Format: JSON-LD](https://img.shields.io/badge/Format-JSON--LD-blue.svg?style=for-the-badge)](https://w3id.org/contro/persp.jsonld)

### Description
An ontology for the perspectivisation frame: a type of events or situations, where a fact (a background) is reported within a certain storytelling (a lens), which creates a viewpoint (a cut), towards which the source (a conceptualiser)  holds a positive, negative, or neutral stance (an attitude).
The result of perspectivisation is not only a linguistic or rhetorical artifice, because it typically involves a 'blending' of the entities playing two roles: the cut, and the lens.

For example, in political talk, when e.g. a democrat says that taxes are investments, the democrat (conceptualiser) holds an attitude towards the current taxation policies (cut from a background), viewed through the generally positive value associated with investments (lens).
The expected result from the example is that a new entity emerges: an 'investment-blended' meaning of taxes.
A lot of public discussions, even in formal contexts, shows perspectivisation situations.

#### Bibliography
A. Gangemi and V. Presutti, “Formal representation and extraction of perspectives,” in *Creating a more transparent internet*. Cambridge: Cambridge University Press, 2022, pp. 208–228, doi: [10.1017/9781108641104.016](https://doi.org/10.1017/9781108641104.016).

### Namespaces

| Prefix | URI |
|--------|-----------|
| base | <https://w3id.org/contro/persp#> |
| d0 | <http://www.ontologydesignpatterns.org/ont/d0.owl#> |
| dc | <http://purl.org/dc/elements/1.1/> |
| dct | <http://purl.org/dc/terms/> |
| dul | <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#> |
| owl | <http://www.w3.org/2002/07/owl#> |
| rdf | <http://www.w3.org/1999/02/22-rdf-syntax-ns#> |
| rdfs | <http://www.w3.org/2000/01/rdf-schema#> |
| vann | <http://purl.org/vocab/vann/> |

## Classes

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Attitude_c">Attitude</h3>
      <a class="class" href="#Attitude_c">https://w3id.org/contro/persp#Attitude</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Attitude_i" title="https://w3id.org/contro/persp#Attitude">Attitude</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#PerspectivisationTheorySituation_c" title="https://w3id.org/contro/persp#PerspectivisationTheorySituation">Perspectivisation theory situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The attitude of a conceptualiser towards an eventuality, perspectivised through the application of a lens, e.g., positive attitude towards taxation policies, reinforced by a positive value such as 'investment' in 'taxes are investiments'.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#Attitude_op" title="https://w3id.org/contro/persp#Attitude">Attitude</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Attitude_op" title="https://w3id.org/contro/persp#Attitude">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#Attitude_i" title="https://w3id.org/contro/persp#Attitude">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Background_c">Background</h3>
      <a class="class" href="#Background_c">https://w3id.org/contro/persp#Background</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Background_i" title="https://w3id.org/contro/persp#Background">Background</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#PerspectivisationTheorySituation_c" title="https://w3id.org/contro/persp#PerspectivisationTheorySituation">Perspectivisation theory situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The background knowledge for an eventuality targeted by perspectivisation, e.g., fiscal knowledge behind current taxation policies in 'taxes are investiments'. In the example, only the background is expressed.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#Background_op" title="https://w3id.org/contro/persp#Background">Background</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Background_op" title="https://w3id.org/contro/persp#Background">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#Background_i" title="https://w3id.org/contro/persp#Background">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Cut_c">Cut</h3>
      <a class="class" href="#Cut_c">https://w3id.org/contro/persp#Cut</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Cut_i" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#PerspectivisationTheorySituation_c" title="https://w3id.org/contro/persp#PerspectivisationTheorySituation">Perspectivisation theory situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The cut emerging from perspectivising an eventuality through a lens, e.g. taxation policies reframed as investments in 'taxes are investiments'.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#Cut_op" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Cut_op" title="https://w3id.org/contro/persp#Cut">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#Cut_i" title="https://w3id.org/contro/persp#Cut">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Eventuality_c">Eventuality</h3>
      <a class="class" href="#Eventuality_c">https://w3id.org/contro/persp#Eventuality</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Eventuality_i" title="https://w3id.org/contro/persp#Eventuality">Eventuality</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/d0.owl#Eventuality" title="http://www.ontologydesignpatterns.org/ont/d0.owl#Eventuality">Eventuality</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="class" href="#PerspectivisationTheorySituation_c" title="https://w3id.org/contro/persp#PerspectivisationTheorySituation">Perspectivisation theory situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The eventuality targeted by perspectivisation, explicitly or implicitly extracted from its background knowledge (e.g., current taxation policies in 'taxes are investiments').</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#Eventuality_op" title="https://w3id.org/contro/persp#Eventuality">Eventuality</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Eventuality_op" title="https://w3id.org/contro/persp#Eventuality">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#Eventuality_i" title="https://w3id.org/contro/persp#Eventuality">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Lens_c">Lens</h3>
      <a class="class" href="#Lens_c">https://w3id.org/contro/persp#Lens</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Lens_i" title="https://w3id.org/contro/persp#Lens">Lens</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#PerspectivisationTheorySituation_c" title="https://w3id.org/contro/persp#PerspectivisationTheorySituation">Perspectivisation theory situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The lens used by perspectivisation on an eventuality, e.g., 'investments' on current taxation policies.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#Lens_op" title="https://w3id.org/contro/persp#Lens">Lens</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Lens_op" title="https://w3id.org/contro/persp#Lens">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#Lens_i" title="https://w3id.org/contro/persp#Lens">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Perspectivisation_c">Perspectivisation</h3>
      <a class="class" href="#Perspectivisation_c">https://w3id.org/contro/persp#Perspectivisation</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Perspectivisation_i" title="https://w3id.org/contro/persp#Perspectivisation">Perspectivisation</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="object_property" href="#Attitude_op" title="https://w3id.org/contro/persp#Attitude">Attitude</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#Background_op" title="https://w3id.org/contro/persp#Background">Background</a><span class="sup" data-text="op" title="Object Property"></span> min 0 <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#Conceptualiser_op" title="https://w3id.org/contro/persp#Conceptualiser">Conceptualiser</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#Cut_op" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#Eventuality_op" title="https://w3id.org/contro/persp#Eventuality">Eventuality</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#Lens_op" title="https://w3id.org/contro/persp#Lens">Lens</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="class" href="#PerspectivisationTheorySituation_c" title="https://w3id.org/contro/persp#PerspectivisationTheorySituation">Perspectivisation theory situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A compositional frame for situations that provide a redescription of an eventuality by using a lens, with an attitude. It usually requires background knowledge for the eventuality (and possibly the lens), as well as one or more agents conceptualising it. 
A 'cut' (in the cinematic sense) emerges from a perspectivisation, which composes an eventuality with a lens, as in the example 'taxes are investments', where current taxation policies (the eventuality) is cut by shooting through the investment lens.
The OWL representation of this frame includes heavy punning: each aspect of a perspectivisation is in fact modeled as a semantic role (holding between perspectivisation situations and the things involved in them, as an individual (the frame projections), as well as classes (the intensional components of the frame), since almost all aspects are frames on their turn.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#composedWith_op" title="https://w3id.org/contro/persp#composedWith">composed with</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>In domain of</h4>
      <li>
        <a class="object_property" href="#composedWith_op" title="https://w3id.org/contro/persp#composedWith">composed with</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="individual" href="#Perspectivisation_i" title="https://w3id.org/contro/persp#Perspectivisation">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="PerspectivisationTheorySituation_c">Perspectivisation theory situation</h3>
      <a class="class" href="#PerspectivisationTheorySituation_c">https://w3id.org/contro/persp#PerspectivisationTheorySituation</a>
    </div>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superclass of</h4>
      <li>
        <a class="class" href="#Attitude_c" title="https://w3id.org/contro/persp#Attitude">Attitude</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Background_c" title="https://w3id.org/contro/persp#Background">Background</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Cut_c" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Eventuality_c" title="https://w3id.org/contro/persp#Eventuality">Eventuality</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Lens_c" title="https://w3id.org/contro/persp#Lens">Lens</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Perspectivisation_c" title="https://w3id.org/contro/persp#Perspectivisation">Perspectivisation</a><span class="sup" data-text="c" title="Class"></span>
      </li>
    </ul>
  </div>
</details>

## Object Properties

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Attitude_op">Attitude</h3>
      <a class="object_property" href="#Attitude_op">https://w3id.org/contro/persp#Attitude</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="#Attitude_c" title="https://w3id.org/contro/persp#Attitude">Attitude</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The attitude of a conceptualiser towards an eventuality, perspectivised through the application of a lens, e.g., positive attitude towards taxation policies, reinforced by a positive value such as 'investment' in 'taxes are investiments'.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is setting for</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="class" href="#Attitude_c" title="https://w3id.org/contro/persp#Attitude">Class</a>
      </li>
      <li>
        <a class="individual" href="#Attitude_i" title="https://w3id.org/contro/persp#Attitude">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Background_op">Background</h3>
      <a class="object_property" href="#Background_op">https://w3id.org/contro/persp#Background</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="#Background_c" title="https://w3id.org/contro/persp#Background">Background</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The background knowledge for an eventuality targeted by perspectivisation, e.g., fiscal knowledge behind current taxation policies in 'taxes are investiments'. In the example, only the background is expressed.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is setting for</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="class" href="#Background_c" title="https://w3id.org/contro/persp#Background">Class</a>
      </li>
      <li>
        <a class="individual" href="#Background_i" title="https://w3id.org/contro/persp#Background">Individual</a>
      </li>
    </ul>
  </div>
</details>

<div class="admonition object_property" markdown>
  <div class="admonition-title overview">
    <div class="label">
      <h3 id="composedWith_op">composed with</h3>
      <a class="object_property" href="#composedWith_op">https://w3id.org/contro/persp#composedWith</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="#Perspectivisation_c" title="https://w3id.org/contro/persp#Perspectivisation">Perspectivisation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="#Perspectivisation_c" title="https://w3id.org/contro/persp#Perspectivisation">Perspectivisation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </div>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Conceptualiser_op">Conceptualiser</h3>
      <a class="object_property" href="#Conceptualiser_op">https://w3id.org/contro/persp#Conceptualiser</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is setting for</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="individual" href="#Conceptualiser_i" title="https://w3id.org/contro/persp#Conceptualiser">Individual</a>
      </li>
    </ul>
  </div>
</details>

<div class="admonition object_property" markdown>
  <div class="admonition-title overview">
    <div class="label">
      <h3 id="contrasts_op">contrasts</h3>
      <a class="object_property" href="#contrasts_op">https://w3id.org/contro/persp#contrasts</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </div>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="creates_op">creates</h3>
      <a class="object_property" href="#creates_op">https://w3id.org/contro/persp#creates</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        inverse(<a class="object_property" href="#holds_op" title="https://w3id.org/contro/persp#holds">holds</a><span class="sup" data-text="op" title="Object Property"></span>) o <a class="object_property" href="#toward_op" title="https://w3id.org/contro/persp#toward">toward</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Cut_op">Cut</h3>
      <a class="object_property" href="#Cut_op">https://w3id.org/contro/persp#Cut</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="#Cut_c" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The cut emerging from perspectivising an eventuality through a lens, e.g. taxation policies reframed as investments in 'taxes are investiments'.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is setting for</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="class" href="#Cut_c" title="https://w3id.org/contro/persp#Cut">Class</a>
      </li>
      <li>
        <a class="individual" href="#Cut_i" title="https://w3id.org/contro/persp#Cut">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Eventuality_op">Eventuality</h3>
      <a class="object_property" href="#Eventuality_op">https://w3id.org/contro/persp#Eventuality</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="#Eventuality_c" title="https://w3id.org/contro/persp#Eventuality">Eventuality</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The eventuality targeted by perspectivisation, explicitly or implicitly extracted from its background knowledge (e.g., current taxation policies in 'taxes are investiments').</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is setting for</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="class" href="#Eventuality_c" title="https://w3id.org/contro/persp#Eventuality">Class</a>
      </li>
      <li>
        <a class="individual" href="#Eventuality_i" title="https://w3id.org/contro/persp#Eventuality">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="extractedFrom_op">extracted from</h3>
      <a class="object_property" href="#extractedFrom_op">https://w3id.org/contro/persp#extractedFrom</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        inverse(<a class="object_property" href="#Eventuality_op" title="https://w3id.org/contro/persp#Eventuality">Eventuality</a><span class="sup" data-text="op" title="Object Property"></span>) o <a class="object_property" href="#Background_op" title="https://w3id.org/contro/persp#Background">Background</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="holds_op">holds</h3>
      <a class="object_property" href="#holds_op">https://w3id.org/contro/persp#holds</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        inverse(<a class="object_property" href="#Conceptualiser_op" title="https://w3id.org/contro/persp#Conceptualiser">Conceptualiser</a><span class="sup" data-text="op" title="Object Property"></span>) o <a class="object_property" href="#Attitude_op" title="https://w3id.org/contro/persp#Attitude">Attitude</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Lens_op">Lens</h3>
      <a class="object_property" href="#Lens_op">https://w3id.org/contro/persp#Lens</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="#Lens_c" title="https://w3id.org/contro/persp#Lens">Lens</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The lens used by perspectivisation on an eventuality, e.g., 'investments' on current taxation policies.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is setting for</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="class" href="#Lens_c" title="https://w3id.org/contro/persp#Lens">Class</a>
      </li>
      <li>
        <a class="individual" href="#Lens_i" title="https://w3id.org/contro/persp#Lens">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="perspectivisedAs_op">perspectivised as</h3>
      <a class="object_property" href="#perspectivisedAs_op">https://w3id.org/contro/persp#perspectivisedAs</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        inverse(<a class="object_property" href="#Eventuality_op" title="https://w3id.org/contro/persp#Eventuality">Eventuality</a><span class="sup" data-text="op" title="Object Property"></span>) o <a class="object_property" href="#Cut_op" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="perspectivisedThrough_op">perspectivised through</h3>
      <a class="object_property" href="#perspectivisedThrough_op">https://w3id.org/contro/persp#perspectivisedThrough</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        inverse(<a class="object_property" href="#Eventuality_op" title="https://w3id.org/contro/persp#Eventuality">Eventuality</a><span class="sup" data-text="op" title="Object Property"></span>) o <a class="object_property" href="#Lens_op" title="https://w3id.org/contro/persp#Lens">Lens</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="shotThrough_op">shot through</h3>
      <a class="object_property" href="#shotThrough_op">https://w3id.org/contro/persp#shotThrough</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        inverse(<a class="object_property" href="#Cut_op" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="op" title="Object Property"></span>) o <a class="object_property" href="#Lens_op" title="https://w3id.org/contro/persp#Lens">Lens</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="toward_op">toward</h3>
      <a class="object_property" href="#toward_op">https://w3id.org/contro/persp#toward</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        inverse(<a class="object_property" href="#Attitude_op" title="https://w3id.org/contro/persp#Attitude">Attitude</a><span class="sup" data-text="op" title="Object Property"></span>) o <a class="object_property" href="#Cut_op" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>



## Individuals

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Attitude_i">Attitude</h3>
      <a class="individual" href="#Attitude_i">https://w3id.org/contro/persp#Attitude</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The attitude of a conceptualiser towards an eventuality, perspectivised through the application of a lens, e.g., positive attitude towards taxation policies, reinforced by a positive value such as 'investment' in 'taxes are investiments'.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Attitude_op" title="https://w3id.org/contro/persp#Attitude">Object Property</a>
      </li>
      <li>
        <a class="class" href="#Attitude_c" title="https://w3id.org/contro/persp#Attitude">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Background_i">Background</h3>
      <a class="individual" href="#Background_i">https://w3id.org/contro/persp#Background</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The background knowledge for an eventuality targeted by perspectivisation, e.g., fiscal knowledge behind current taxation policies in 'taxes are investiments'. In the example, only the background is expressed.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Background_op" title="https://w3id.org/contro/persp#Background">Object Property</a>
      </li>
      <li>
        <a class="class" href="#Background_c" title="https://w3id.org/contro/persp#Background">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Conceptualiser_i">Conceptualiser</h3>
      <a class="individual" href="#Conceptualiser_i">https://w3id.org/contro/persp#Conceptualiser</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Conceptualiser_op" title="https://w3id.org/contro/persp#Conceptualiser">Object Property</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Cut_i">Cut</h3>
      <a class="individual" href="#Cut_i">https://w3id.org/contro/persp#Cut</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The cut emerging from perspectivising an eventuality through a lens, e.g. taxation policies reframed as investments in 'taxes are investiments'.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Cut_op" title="https://w3id.org/contro/persp#Cut">Object Property</a>
      </li>
      <li>
        <a class="class" href="#Cut_c" title="https://w3id.org/contro/persp#Cut">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Eventuality_i">Eventuality</h3>
      <a class="individual" href="#Eventuality_i">https://w3id.org/contro/persp#Eventuality</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The eventuality targeted by perspectivisation, explicitly or implicitly extracted from its background knowledge (e.g., current taxation policies in 'taxes are investiments').</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Eventuality_op" title="https://w3id.org/contro/persp#Eventuality">Object Property</a>
      </li>
      <li>
        <a class="class" href="#Eventuality_c" title="https://w3id.org/contro/persp#Eventuality">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Lens_i">Lens</h3>
      <a class="individual" href="#Lens_i">https://w3id.org/contro/persp#Lens</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The lens used by perspectivisation on an eventuality, e.g., 'investments' on current taxation policies.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Lens_op" title="https://w3id.org/contro/persp#Lens">Object Property</a>
      </li>
      <li>
        <a class="class" href="#Lens_c" title="https://w3id.org/contro/persp#Lens">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Perspectivisation_i">Perspectivisation</h3>
      <a class="individual" href="#Perspectivisation_i">https://w3id.org/contro/persp#Perspectivisation</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A compositional frame for situations that provide a redescription of an eventuality by using a lens, with an attitude. It usually requires background knowledge for the eventuality (and possibly the lens), as well as one or more agents conceptualising it. 
A 'cut' (in the cinematic sense) emerges from a perspectivisation, which composes an eventuality with a lens, as in the example 'taxes are investments', where current taxation policies (the eventuality) is cut by shooting through the investment lens.
The OWL representation of this frame includes heavy punning: each aspect of a perspectivisation is in fact modeled as a semantic role (holding between perspectivisation situations and the things involved in them, as an individual (the frame projections), as well as classes (the intensional components of the frame), since almost all aspects are frames on their turn.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Assertions</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Attitude_i" title="https://w3id.org/contro/persp#Attitude">Attitude</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Background_i" title="https://w3id.org/contro/persp#Background">Background</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Conceptualiser_i" title="https://w3id.org/contro/persp#Conceptualiser">Conceptualiser</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Cut_i" title="https://w3id.org/contro/persp#Cut">Cut</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Eventuality_i" title="https://w3id.org/contro/persp#Eventuality">Eventuality</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Lens_i" title="https://w3id.org/contro/persp#Lens">Lens</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="class" href="#Perspectivisation_c" title="https://w3id.org/contro/persp#Perspectivisation">Class</a>
      </li>
    </ul>
  </div>
</details>



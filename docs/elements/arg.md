<!--- This file was automatically generated - do not edit -->

<h1>Argumentation Ontology <small>(arg)</small></h1>

## Overview

**IRI:** <https://w3id.org/contro/arg>

**Version:** 0.6

**Release:** 12/03/2025

**Last update:** 03/06/2025

**Authors:** Alberto Ciarrocca, Francesca Massarenti

**License:** [![License: CC BY 4.0](https://img.shields.io/badge/-CC%20BY%204.0-lightgrey.svg?style=for-the-badge)](https://creativecommons.org/licenses/by/4.0/)

**Available:**

[![Format: TTL](https://img.shields.io/badge/Format-TTL-green.svg?style=for-the-badge)](https://w3id.org/contro/arg.ttl)
[![Format: XML/RDF](https://img.shields.io/badge/Format-XML/RDF-red.svg?style=for-the-badge)](https://w3id.org/contro/arg.owl)
[![Format: JSON-LD](https://img.shields.io/badge/Format-JSON--LD-blue.svg?style=for-the-badge)](https://w3id.org/contro/arg.jsonld)

### Description
Reconstruct argumentative structures in text.

#### Bibliography
S. Modgil and H. Prakken. “A general account of argumentation with preferences.” *Artificial Intelligence*, vol. 195, 1 Feb. 2013, pp. 361–97, doi: [10.1016/j.artint.2012.10.008](https://doi.org/10.1016/j.artint.2012.10.008).

### Namespaces

| Prefix | URI |
|--------|-----------|
| base | <https://w3id.org/contro/arg#> |
| d0 | <http://www.ontologydesignpatterns.org/ont/d0.owl#> |
| dc | <http://purl.org/dc/elements/1.1/> |
| dct | <http://purl.org/dc/terms/> |
| dul | <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#> |
| owl | <http://www.w3.org/2002/07/owl#> |
| rdf | <http://www.w3.org/1999/02/22-rdf-syntax-ns#> |
| rdfs | <http://www.w3.org/2000/01/rdf-schema#> |
| swrl | <http://www.w3.org/2003/11/swrl#> |
| swrla | <http://swrl.stanford.edu/ontologies/3.3/swrla.owl#> |
| vann | <http://purl.org/vocab/vann/> |

## Classes

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="AcceptanceAttitude_c">Acceptance Attitude</h3>
      <a class="class" href="#AcceptanceAttitude_c">https://w3id.org/contro/arg#AcceptanceAttitude</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#AcceptanceAttitude_i" title="https://w3id.org/contro/arg#AcceptanceAttitude">Acceptance Attitude</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The attitude a dialogical agent holds toward the argument of another agent. Depending on their acceptance attitude, an agent may accept the premises and/or conclusion, respond with a counterargument, or ask for further grounds for a premise.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#AcceptanceAttitude_op" title="https://w3id.org/contro/arg#AcceptanceAttitude">Acceptance Attitude</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#AcceptanceAttitude_op" title="https://w3id.org/contro/arg#AcceptanceAttitude">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#AcceptanceAttitude_i" title="https://w3id.org/contro/arg#AcceptanceAttitude">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Antecedent_c">Antecedent</h3>
      <a class="class" href="#Antecedent_c">https://w3id.org/contro/arg#Antecedent</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Antecedent_i" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">One of the formulas that make up the first half of an inference rule, each expressing part of the condition for its application.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#Antecedent_i" title="https://w3id.org/contro/arg#Antecedent">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Argument_c">Argument</h3>
      <a class="class" href="#Argument_c">https://w3id.org/contro/arg#Argument</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Argument_i" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="object_property" href="#ArgumentationTheory_op" title="https://w3id.org/contro/arg#ArgumentationTheory">Argumentation Theory</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#ArgumentationTheory_c" title="https://w3id.org/contro/arg#ArgumentationTheory">Argumentation Theory</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#Conclusion_c" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> min 0 <a class="class" href="#Premise_c" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#Topic_op" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/d0.owl#Eventuality" title="http://www.ontologydesignpatterns.org/ont/d0.owl#Eventuality">Eventuality</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A structure built from a set of premises, a conclusion, and an inference rule connecting them. It is generated by an agent's argumentation theory on the basis of their knowledge base.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superclass of</h4>
      <li>
        <a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#DefeasibleInference_c" title="https://w3id.org/contro/arg#DefeasibleInference">Defeasible Inference</a><span class="sup" data-text="c" title="Class"></span>
      </li>
    </ul>
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#attacks_op" title="https://w3id.org/contro/arg#attacks">attacks</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
      <li>
        <a class="object_property" href="#defends_op" title="https://w3id.org/contro/arg#defends">defends</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
      <li>
        <a class="object_property" href="#hasSubArgument_op" title="https://w3id.org/contro/arg#hasSubArgument">has Sub-Argument</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>In domain of</h4>
      <li>
        <a class="object_property" href="#by_op" title="https://w3id.org/contro/arg#by">by</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
      <li>
        <a class="object_property" href="#defends_op" title="https://w3id.org/contro/arg#defends">defends</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
      <li>
        <a class="object_property" href="#hasSubArgument_op" title="https://w3id.org/contro/arg#hasSubArgument">has Sub-Argument</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Disjoint with</h4>
      <li>
        <a class="class" href="#ArgumentationTheory_c" title="https://w3id.org/contro/arg#ArgumentationTheory">Argumentation Theory</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#KnowledgeBase_c" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="c" title="Class"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="individual" href="#Argument_i" title="https://w3id.org/contro/arg#Argument">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="ArgumentationTheory_c">Argumentation Theory</h3>
      <a class="class" href="#ArgumentationTheory_c">https://w3id.org/contro/arg#ArgumentationTheory</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#ArgumentationTheory_i" title="https://w3id.org/contro/arg#ArgumentationTheory">Argumentation Theory</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#DialogicalAgent_op" title="https://w3id.org/contro/arg#DialogicalAgent">Dialogical Agent</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#KnowledgeBase_op" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="op" title="Object Property"></span> min 0 <a class="class" href="#KnowledgeBase_c" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">An agent's argumentation theory is the combination of their knowledge base and acceptance attitude, relative to which arguments are generated and evaluated.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#ArgumentationTheory_op" title="https://w3id.org/contro/arg#ArgumentationTheory">Argumentation Theory</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Disjoint with</h4>
      <li>
        <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#ArgumentationTheory_op" title="https://w3id.org/contro/arg#ArgumentationTheory">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#ArgumentationTheory_i" title="https://w3id.org/contro/arg#ArgumentationTheory">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="ArgumentationTheorySituation_c">Argumentation Theory Situation</h3>
      <a class="class" href="#ArgumentationTheorySituation_c">https://w3id.org/contro/arg#ArgumentationTheorySituation</a>
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
        <a class="class" href="#AcceptanceAttitude_c" title="https://w3id.org/contro/arg#AcceptanceAttitude">Acceptance Attitude</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Antecedent_c" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#ArgumentationTheory_c" title="https://w3id.org/contro/arg#ArgumentationTheory">Argumentation Theory</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Conclusion_c" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Consequent_c" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#KnowledgeBase_c" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Premise_c" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="c" title="Class"></span>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Conclusion_c">Conclusion</h3>
      <a class="class" href="#Conclusion_c">https://w3id.org/contro/arg#Conclusion</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Conclusion_i" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The claim of an argument, following from its constituent premises and rule application. It may contradict another argument's premise, inference rule application or conclusion.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>In domain of</h4>
      <li>
        <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Disjoint with</h4>
      <li>
        <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="c" title="Class"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#Conclusion_i" title="https://w3id.org/contro/arg#Conclusion">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Conflict_c">Conflict</h3>
      <a class="class" href="#Conflict_c">https://w3id.org/contro/arg#Conflict</a>
    </div>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="#attacks_op" title="https://w3id.org/contro/arg#attacks">attacks</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">They can only target at fallible elements of an argument: their uncertain premises, their defeasible inferences, or the conclusions of their defeasible inferences.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superclass of</h4>
      <li>
        <a class="class" href="#Rebuttal_c" title="https://w3id.org/contro/arg#Rebuttal">Rebuttal</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Undercut_c" title="https://w3id.org/contro/arg#Undercut">Undercut</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Undermining_c" title="https://w3id.org/contro/arg#Undermining">Undermining</a><span class="sup" data-text="c" title="Class"></span>
      </li>
    </ul>
    <ul>
      <h4>In domain of</h4>
      <li>
        <a class="object_property" href="#attacks_op" title="https://w3id.org/contro/arg#attacks">attacks</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Consequent_c">Consequent</h3>
      <a class="class" href="#Consequent_c">https://w3id.org/contro/arg#Consequent</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Consequent_i" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The formula that makes up the second half of an inference rule and is inferred when the antecedents are satisfied.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#Consequent_i" title="https://w3id.org/contro/arg#Consequent">Individual</a>
      </li>
    </ul>
  </div>
</details>

<div class="admonition class" markdown>
  <div class="admonition-title overview">
    <div class="label">
      <h3 id="DefeasibleInference_c">Defeasible Inference</h3>
      <a class="class" href="#DefeasibleInference_c">https://w3id.org/contro/arg#DefeasibleInference</a>
    </div>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">An argument that draws its conclusion by applying at least one defeasible inference rule. It can be attacked on its rule application and may be defeated even if all its premises hold, since the support it provides for the conclusion is presumptive rather than deductive.</p>
  </div>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="InferenceRule_c">Inference Rule</h3>
      <a class="class" href="#InferenceRule_c">https://w3id.org/contro/arg#InferenceRule</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span> min 0 <a class="class" href="#Antecedent_c" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="c" title="Class"></span> and <br/><a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span> exactly 1 <a class="class" href="#Consequent_c" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#InferenceRule_i" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A way of drawing a conclusion from a set of premises. When applied in an argument, the antecedents of the rule serve as premises and the consequent as the conclusion.
It may express a general principle of reasoning or encode domain-specific knowledge as a scheme in which the rule’s antecedents and consequent are formulas about a term (topic).
Inference rules, together with premises, form part of the dialogical agent’s knowledge base.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Disjoint with</h4>
      <li>
        <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Conclusion_c" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="c" title="Class"></span>
      </li>
      <li>
        <a class="class" href="#Premise_c" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="c" title="Class"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#InferenceRule_i" title="https://w3id.org/contro/arg#InferenceRule">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="KnowledgeBase_c">Knowledge Base</h3>
      <a class="class" href="#KnowledgeBase_c">https://w3id.org/contro/arg#KnowledgeBase</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#KnowledgeBase_i" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The set of premises and inference rules available to an agent for constructing arguments.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#KnowledgeBase_op" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Disjoint with</h4>
      <li>
        <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#KnowledgeBase_op" title="https://w3id.org/contro/arg#KnowledgeBase">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#KnowledgeBase_i" title="https://w3id.org/contro/arg#KnowledgeBase">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="class" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Premise_c">Premise</h3>
      <a class="class" href="#Premise_c">https://w3id.org/contro/arg#Premise</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Premise_i" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A formula that supports the conclusion of an argument. It may either be extracted from the knowledge base or derived as the conclusion of another argument.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>In range of</h4>
      <li>
        <a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Disjoint with</h4>
      <li>
        <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="c" title="Class"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Object Property</a>
      </li>
      <li>
        <a class="individual" href="#Premise_i" title="https://w3id.org/contro/arg#Premise">Individual</a>
      </li>
    </ul>
  </div>
</details>

<div class="admonition class" markdown>
  <div class="admonition-title overview">
    <div class="label">
      <h3 id="Rebuttal_c">Rebuttal</h3>
      <a class="class" href="#Rebuttal_c">https://w3id.org/contro/arg#Rebuttal</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> some (<a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#Conclusion_c" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="c" title="Class"></span>)
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A rebuttal is a conflict that attacks an argument on its conclusion, providing an alternative one.</p>
  </div>

<div class="admonition class" markdown>
  <div class="admonition-title overview">
    <div class="label">
      <h3 id="Undercut_c">Undercut</h3>
      <a class="class" href="#Undercut_c">https://w3id.org/contro/arg#Undercut</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> some (<a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="c" title="Class"></span>)
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">An undercut is a conflict that attacks an argument on its inference rule.</p>
  </div>

<div class="admonition class" markdown>
  <div class="admonition-title overview">
    <div class="label">
      <h3 id="Undermining_c">Undermining</h3>
      <a class="class" href="#Undermining_c">https://w3id.org/contro/arg#Undermining</a>
    </div>
  <ul>
    <h4>Equivalent to</h4>
    <li>
      <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> some (<a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#Premise_c" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="c" title="Class"></span>)
    </li>
  </ul>
  <ul>
    <h4>Subclass of</h4>
    <li>
      <a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">An undermining is a conflict that attacks an argument on its premise.</p>
  </div>

## Object Properties

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="AcceptanceAttitude_op">Acceptance Attitude</h3>
      <a class="object_property" href="#AcceptanceAttitude_op">https://w3id.org/contro/arg#AcceptanceAttitude</a>
    </div>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="#AcceptanceAttitude_c" title="https://w3id.org/contro/arg#AcceptanceAttitude">Acceptance Attitude</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The attitude a dialogical agent holds toward the argument of another agent. Depending on their acceptance attitude, an agent may accept the premises and/or conclusion, respond with a counterargument, or ask for further grounds for a premise.</p>
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
        <a class="class" href="#AcceptanceAttitude_c" title="https://w3id.org/contro/arg#AcceptanceAttitude">Class</a>
      </li>
      <li>
        <a class="individual" href="#AcceptanceAttitude_i" title="https://w3id.org/contro/arg#AcceptanceAttitude">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Antecedent_op">Antecedent</h3>
      <a class="object_property" href="#Antecedent_op">https://w3id.org/contro/arg#Antecedent</a>
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
      <a class="class" href="#Antecedent_c" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">One of the formulas that make up the first half of an inference rule, each expressing part of the condition for its application.</p>
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
        <a class="class" href="#Antecedent_c" title="https://w3id.org/contro/arg#Antecedent">Class</a>
      </li>
      <li>
        <a class="individual" href="#Antecedent_i" title="https://w3id.org/contro/arg#Antecedent">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="ArgumentationTheory_op">Argumentation Theory</h3>
      <a class="object_property" href="#ArgumentationTheory_op">https://w3id.org/contro/arg#ArgumentationTheory</a>
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
      <a class="class" href="#ArgumentationTheory_c" title="https://w3id.org/contro/arg#ArgumentationTheory">Argumentation Theory</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">An agent's argumentation theory is the combination of their knowledge base and acceptance attitude, relative to which arguments are generated and evaluated.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is setting for</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        <a class="object_property" href="#by_op" title="https://w3id.org/contro/arg#by">by</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#DialogicalAgent_op" title="https://w3id.org/contro/arg#DialogicalAgent">Dialogical Agent</a><span class="sup" data-text="op" title="Object Property"></span>)
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="class" href="#ArgumentationTheory_c" title="https://w3id.org/contro/arg#ArgumentationTheory">Class</a>
      </li>
      <li>
        <a class="individual" href="#ArgumentationTheory_i" title="https://w3id.org/contro/arg#ArgumentationTheory">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="attackedBy_op">attacked by</h3>
      <a class="object_property" href="#attackedBy_op">https://w3id.org/contro/arg#attackedBy</a>
    </div>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Inverse of</h4>
      <li>
        <a class="object_property" href="#attacks_op" title="https://w3id.org/contro/arg#attacks">attacks</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="attacks_op">attacks</h3>
      <a class="object_property" href="#attacks_op">https://w3id.org/contro/arg#attacks</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Inverse of</h4>
      <li>
        <a class="object_property" href="#attackedBy_op" title="https://w3id.org/contro/arg#attackedBy">attacked by</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span>) o inverse(<a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="op" title="Object Property"></span>)
      </li>
      <li>
        <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span>)
      </li>
      <li>
        <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span>) o inverse(<a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="op" title="Object Property"></span>)
      </li>
      <li>
        <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="op" title="Object Property"></span>)
      </li>
      <li>
        <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span>)
      </li>
      <li>
        <a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span>)
      </li>
      <li>
        <a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span>)
      </li>
    </ul>
  </div>
</details>

<div class="admonition object_property" markdown>
  <div class="admonition-title overview">
    <div class="label">
      <h3 id="by_op">by</h3>
      <a class="object_property" href="#by_op">https://w3id.org/contro/arg#by</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </div>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Conclusion_op">Conclusion</h3>
      <a class="object_property" href="#Conclusion_op">https://w3id.org/contro/arg#Conclusion</a>
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
      <a class="class" href="#Conclusion_c" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The claim of an argument, following from its constituent premises and rule application. It may contradict another argument's premise, inference rule application or conclusion.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is setting for</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        <a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="class" href="#Conclusion_c" title="https://w3id.org/contro/arg#Conclusion">Class</a>
      </li>
      <li>
        <a class="individual" href="#Conclusion_i" title="https://w3id.org/contro/arg#Conclusion">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Consequent_op">Consequent</h3>
      <a class="object_property" href="#Consequent_op">https://w3id.org/contro/arg#Consequent</a>
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
      <a class="class" href="#Consequent_c" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The formula that makes up the second half of an inference rule and is inferred when the antecedents are satisfied.</p>
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
        <a class="class" href="#Consequent_c" title="https://w3id.org/contro/arg#Consequent">Class</a>
      </li>
      <li>
        <a class="individual" href="#Consequent_i" title="https://w3id.org/contro/arg#Consequent">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="contradictedBy_op">contradicted by</h3>
      <a class="object_property" href="#contradictedBy_op">https://w3id.org/contro/arg#contradictedBy</a>
    </div>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Inverse of</h4>
      <li>
        <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="contradicts_op">contradicts</h3>
      <a class="object_property" href="#contradicts_op">https://w3id.org/contro/arg#contradicts</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="#Conclusion_c" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="#Conclusion_c" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="c" title="Class"></span> or <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="c" title="Class"></span> or <a class="class" href="#Premise_c" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Inverse of</h4>
      <li>
        <a class="object_property" href="#contradictedBy_op" title="https://w3id.org/contro/arg#contradictedBy">contradicted by</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="defends_op">defends</h3>
      <a class="object_property" href="#defends_op">https://w3id.org/contro/arg#defends</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">Irreflexive</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        <a class="object_property" href="#attacks_op" title="https://w3id.org/contro/arg#attacks">attacks</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#attacks_op" title="https://w3id.org/contro/arg#attacks">attacks</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="DialogicalAgent_op">Dialogical Agent</h3>
      <a class="object_property" href="#DialogicalAgent_op">https://w3id.org/contro/arg#DialogicalAgent</a>
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
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasRole" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasRole">has role</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#DialogicalAgent_i" title="https://w3id.org/contro/arg#DialogicalAgent">Dialogical Agent</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  </div>
  <p class="description">An agent who takes part in a spoken or written interaction.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is setting for</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        <a class="object_property" href="#DialogicalAgent_op" title="https://w3id.org/contro/arg#DialogicalAgent">Dialogical Agent</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#isAliasOf_op" title="https://w3id.org/contro/arg#isAliasOf">is alias of</a><span class="sup" data-text="op" title="Object Property"></span>)
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="individual" href="#DialogicalAgent_i" title="https://w3id.org/contro/arg#DialogicalAgent">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="extractedFrom_op">extracted from</h3>
      <a class="object_property" href="#extractedFrom_op">https://w3id.org/contro/arg#extractedFrom</a>
    </div>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        inverse(<a class="object_property" href="#hasMember_op" title="https://w3id.org/contro/arg#hasMember">has member</a><span class="sup" data-text="op" title="Object Property"></span>)
      </li>
    </ul>
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        inverse(<a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="op" title="Object Property"></span>) o <a class="object_property" href="#ArgumentationTheory_op" title="https://w3id.org/contro/arg#ArgumentationTheory">Argumentation Theory</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#KnowledgeBase_op" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
      <li>
        inverse(<a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span>) o <a class="object_property" href="#ArgumentationTheory_op" title="https://w3id.org/contro/arg#ArgumentationTheory">Argumentation Theory</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#KnowledgeBase_op" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="hasMember_op">has member</h3>
      <a class="object_property" href="#hasMember_op">https://w3id.org/contro/arg#hasMember</a>
    </div>
  </div>
  </summary>
  <div class="extra">
    <ul>
      <h4>See also</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasMember" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasMember">has member</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="hasSubArgument_op">has Sub-Argument</h3>
      <a class="object_property" href="#hasSubArgument_op">https://w3id.org/contro/arg#hasSubArgument</a>
    </div>
  <ul>
    <h4>Domain</h4>
    <li>
      <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  <ul>
    <h4>Range</h4>
    <li>
      <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A transitive relation between arguments, where one argument has as sub-argument the other if it derives one of its premises from the other’s conclusion. If the sub-argument argument is defeated, so is the dependent argument.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        <a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span>)
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="InferenceRule_op">Inference Rule</h3>
      <a class="object_property" href="#InferenceRule_op">https://w3id.org/contro/arg#InferenceRule</a>
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
      <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A way of drawing a conclusion from a set of premises. When applied in an argument, the antecedents of the rule serve as premises and the consequent as the conclusion.
It may express a general principle of reasoning or encode domain-specific knowledge as a scheme in which the rule’s antecedents and consequent are formulas about a term (topic).
Inference rules, together with premises, form part of the dialogical agent’s knowledge base.</p>
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
        <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Class</a>
      </li>
      <li>
        <a class="individual" href="#InferenceRule_i" title="https://w3id.org/contro/arg#InferenceRule">Individual</a>
      </li>
    </ul>
  </div>
</details>

<div class="admonition object_property" markdown>
  <div class="admonition-title overview">
    <div class="label">
      <h3 id="isAliasOf_op">is alias of</h3>
      <a class="object_property" href="#isAliasOf_op">https://w3id.org/contro/arg#isAliasOf</a>
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
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  </div>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="KnowledgeBase_op">Knowledge Base</h3>
      <a class="object_property" href="#KnowledgeBase_op">https://w3id.org/contro/arg#KnowledgeBase</a>
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
      <a class="class" href="#KnowledgeBase_c" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The set of premises and inference rules available to an agent for constructing arguments.</p>
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
        <a class="class" href="#KnowledgeBase_c" title="https://w3id.org/contro/arg#KnowledgeBase">Class</a>
      </li>
      <li>
        <a class="individual" href="#KnowledgeBase_i" title="https://w3id.org/contro/arg#KnowledgeBase">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Premise_op">Premise</h3>
      <a class="object_property" href="#Premise_op">https://w3id.org/contro/arg#Premise</a>
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
      <a class="class" href="#Premise_c" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A formula that supports the conclusion of an argument. It may either be extracted from the knowledge base or derived as the conclusion of another argument.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Subproperty of</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is setting for</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Superproperty of chain</h4>
      <li>
        <a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="class" href="#Premise_c" title="https://w3id.org/contro/arg#Premise">Class</a>
      </li>
      <li>
        <a class="individual" href="#Premise_i" title="https://w3id.org/contro/arg#Premise">Individual</a>
      </li>
    </ul>
  </div>
</details>

<details class="object_property" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Topic_op">Topic</h3>
      <a class="object_property" href="#Topic_op">https://w3id.org/contro/arg#Topic</a>
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
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/d0.owl#Eventuality" title="http://www.ontologydesignpatterns.org/ont/d0.owl#Eventuality">Eventuality</a><span class="sup" data-text="c" title="Class"></span>
    </li>
    <li>
      <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasRole" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasRole">has role</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Topic_i" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="sup" data-text="i" title="Individual"></span>
    </li>
  </ul>
  </div>
  <p class="description">What the argument is about, as opposed to what is being said about it. It can be understood as a term that appears in both the premises and the conclusion.</p>
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
        <a class="individual" href="#Topic_i" title="https://w3id.org/contro/arg#Topic">Individual</a>
      </li>
    </ul>
  </div>
</details>



## Individuals

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="AcceptanceAttitude_i">Acceptance Attitude</h3>
      <a class="individual" href="#AcceptanceAttitude_i">https://w3id.org/contro/arg#AcceptanceAttitude</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The attitude a dialogical agent holds toward the argument of another agent. Depending on their acceptance attitude, an agent may accept the premises and/or conclusion, respond with a counterargument, or ask for further grounds for a premise.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#AcceptanceAttitude_op" title="https://w3id.org/contro/arg#AcceptanceAttitude">Object Property</a>
      </li>
      <li>
        <a class="class" href="#AcceptanceAttitude_c" title="https://w3id.org/contro/arg#AcceptanceAttitude">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Antecedent_i">Antecedent</h3>
      <a class="individual" href="#Antecedent_i">https://w3id.org/contro/arg#Antecedent</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">One of the formulas that make up the first half of an inference rule, each expressing part of the condition for its application.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Object Property</a>
      </li>
      <li>
        <a class="class" href="#Antecedent_c" title="https://w3id.org/contro/arg#Antecedent">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Argument_i">Argument</h3>
      <a class="individual" href="#Argument_i">https://w3id.org/contro/arg#Argument</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A structure built from a set of premises, a conclusion, and an inference rule connecting them. It is generated by an agent's argumentation theory on the basis of their knowledge base.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Assertions</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#definesRole" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#definesRole">defines role</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Topic_i" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#ArgumentationTheory_i" title="https://w3id.org/contro/arg#ArgumentationTheory">Argumentation Theory</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Conclusion_i" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#InferenceRule_i" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Premise_i" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="ArgumentationTheory_i">Argumentation Theory</h3>
      <a class="individual" href="#ArgumentationTheory_i">https://w3id.org/contro/arg#ArgumentationTheory</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">An agent's argumentation theory is the combination of their knowledge base and acceptance attitude, relative to which arguments are generated and evaluated.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Assertions</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#definesRole" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#definesRole">defines role</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#DialogicalAgent_i" title="https://w3id.org/contro/arg#DialogicalAgent">Dialogical Agent</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#AcceptanceAttitude_i" title="https://w3id.org/contro/arg#AcceptanceAttitude">Acceptance Attitude</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#KnowledgeBase_i" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#ArgumentationTheory_op" title="https://w3id.org/contro/arg#ArgumentationTheory">Object Property</a>
      </li>
      <li>
        <a class="class" href="#ArgumentationTheory_c" title="https://w3id.org/contro/arg#ArgumentationTheory">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Conclusion_i">Conclusion</h3>
      <a class="individual" href="#Conclusion_i">https://w3id.org/contro/arg#Conclusion</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The claim of an argument, following from its constituent premises and rule application. It may contradict another argument's premise, inference rule application or conclusion.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Object Property</a>
      </li>
      <li>
        <a class="class" href="#Conclusion_c" title="https://w3id.org/contro/arg#Conclusion">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Consequent_i">Consequent</h3>
      <a class="individual" href="#Consequent_i">https://w3id.org/contro/arg#Consequent</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The formula that makes up the second half of an inference rule and is inferred when the antecedents are satisfied.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Object Property</a>
      </li>
      <li>
        <a class="class" href="#Consequent_c" title="https://w3id.org/contro/arg#Consequent">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="DialogicalAgent_i">Dialogical Agent</h3>
      <a class="individual" href="#DialogicalAgent_i">https://w3id.org/contro/arg#DialogicalAgent</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Role" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Role">Role</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">An agent who takes part in a spoken or written interaction.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#DialogicalAgent_op" title="https://w3id.org/contro/arg#DialogicalAgent">Object Property</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="InferenceRule_i">Inference Rule</h3>
      <a class="individual" href="#InferenceRule_i">https://w3id.org/contro/arg#InferenceRule</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A way of drawing a conclusion from a set of premises. When applied in an argument, the antecedents of the rule serve as premises and the consequent as the conclusion.
It may express a general principle of reasoning or encode domain-specific knowledge as a scheme in which the rule’s antecedents and consequent are formulas about a term (topic).
Inference rules, together with premises, form part of the dialogical agent’s knowledge base.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Assertions</h4>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Antecedent_i" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
      <li>
        <a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Consequent_i" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="i" title="Individual"></span>
      </li>
    </ul>
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Object Property</a>
      </li>
      <li>
        <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="KnowledgeBase_i">Knowledge Base</h3>
      <a class="individual" href="#KnowledgeBase_i">https://w3id.org/contro/arg#KnowledgeBase</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">The set of premises and inference rules available to an agent for constructing arguments.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#KnowledgeBase_op" title="https://w3id.org/contro/arg#KnowledgeBase">Object Property</a>
      </li>
      <li>
        <a class="class" href="#KnowledgeBase_c" title="https://w3id.org/contro/arg#KnowledgeBase">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Premise_i">Premise</h3>
      <a class="individual" href="#Premise_i">https://w3id.org/contro/arg#Premise</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">A formula that supports the conclusion of an argument. It may either be extracted from the knowledge base or derived as the conclusion of another argument.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Object Property</a>
      </li>
      <li>
        <a class="class" href="#Premise_c" title="https://w3id.org/contro/arg#Premise">Class</a>
      </li>
    </ul>
  </div>
</details>

<details class="individual" name="element" markdown>
  <summary>
  <div class="overview">
    <div class="label">
      <h3 id="Topic_i">Topic</h3>
      <a class="individual" href="#Topic_i">https://w3id.org/contro/arg#Topic</a>
    </div>
  <ul>
    <h4>Class</h4>
    <li>
      <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Role" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Role">Role</a><span class="sup" data-text="c" title="Class"></span>
    </li>
  </ul>
  </div>
  <p class="description">What the argument is about, as opposed to what is being said about it. It can be understood as a term that appears in both the premises and the conclusion.</p>
  </summary>
  <div class="extra">
    <ul>
      <h4>Also defined as</h4>
      <li>
        <a class="object_property" href="#Topic_op" title="https://w3id.org/contro/arg#Topic">Object Property</a>
      </li>
    </ul>
  </div>
</details>

## Rules

<div class="admonition rule" markdown>
  <div class="admonition-title overview">
    <div class="label">
      <h3 id="Implicit_Inference_Rule">Implicit Inference Rule</h3>
    </div>
  </div>
  <p class="description">An argument that concludes B from A has the implicit rule that there exists an implication from A to B.</p>
  <p><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span>(?arg, ?prem) ∧ <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span>(?arg, ?conc) ∧ <a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span>(?rule, ?prem) ∧ <a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span>(?rule, ?conc) → <a class="object_property" href="#InferenceRule_op" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="op" title="Object Property"></span>(?arg, ?rule)</p>
  </div>


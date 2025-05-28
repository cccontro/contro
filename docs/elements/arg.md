<h1>The argumentation ontology <smaller>(arg)</smaller></h1>

## Overview

**IRI:** <https://w3id.org/contro/arg>

**Version:** 0.5.0

**Release:** 12/03/2025

**Last update:** 21/05/2025

**Authors:** Alberto Ciarrocca, Francesca Massarenti


**License:** [![License: CC BY 4.0](https://img.shields.io/badge/-CC%20BY%204.0-lightgrey.svg?style=for-the-badge)](https://creativecommons.org/licenses/by/4.0/)

**Available:**

[![Format: TTL](https://img.shields.io/badge/Format-TTL-green.svg?style=for-the-badge)](https://w3id.org/contro/arg.ttl)
[![Format: XML/RDF](https://img.shields.io/badge/Format-XML/RDF-red.svg?style=for-the-badge)](https://w3id.org/contro/arg.owl)
[![Format: JSON LD](https://img.shields.io/badge/Format-JSON_LD-blue.svg?style=for-the-badge)](https://w3id.org/contro/arg.json-ld)

### Description
The Argumentation ontology can be used to reconstruct argumentative structures in text.

### Namespaces

| Prefix | URI |
|--------|-----------|
| base | <https://w3id.org/contro/arg#> |
| d0 | <http://www.ontologydesignpatterns.org/ont/d0.owl#> |
| dc | <http://purl.org/dc/elements/1.1/> |
| dct | <http://purl.org/dc/terms/> |
| dul | <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#> |
| owl | <http://www.w3.org/2002/07/owl#> |
| persp | <https://w3id.org/contro/persp#> |
| rdf | <http://www.w3.org/1999/02/22-rdf-syntax-ns#> |
| rdfs | <http://www.w3.org/2000/01/rdf-schema#> |
| swrl | <http://www.w3.org/2003/11/swrl#> |
| swrla | <http://swrl.stanford.edu/ontologies/3.3/swrla.owl#> |
| vann | <http://purl.org/vocab/vann/> |

## Classes

<details class="class" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Argument_c">Argument</h3>
<a class="class" href="#Argument_c">https://w3id.org/contro/arg#Argument</a>
</div>

<ul>
  <h4>Equivalent to</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Argument_i" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>
<ul>
  <h4>Subclass of</h4>
  <li><a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="object_property" href="#Author_op" title="https://w3id.org/contro/arg#Author">Author</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> max 1 <a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="object_property" href="#KnowledgeBase_op" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="op" title="Object Property"></span> min 0 <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="object_property" href="#Topic_op" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">An argument is defined relative to an argumentation theory and a knowledge base. Its premises are the formulas and inference rule from the knowledge base, its conclusion is the formula inferred from the premises through the application of said inference rule.</p>


</summary>
<div class="extra">

<ul>
  <h4>Superclass of</h4>
  <li><a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>In range of</h4>
  <li><a class="object_property" href="#attacks_op" title="https://w3id.org/contro/arg#attacks">attacks</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>
<ul>
  <h4>Disjoint with</h4>
  <li><a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>

<ul>
<h4>Also defined as</h4>
<li>
<a class="individual" href="#Argument_i" title="https://w3id.org/contro/arg#Argument">Individual</a>
</li>
</ul>

</div>
</details>
  
<details class="class" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="ArgumentationTheorySituation_c">Argumentation Theory Situation</h3>
<a class="class" href="#ArgumentationTheorySituation_c">https://w3id.org/contro/arg#ArgumentationTheorySituation</a>
</div>

<ul>
  <h4>Subclass of</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>



</summary>
<div class="extra">

<ul>
  <h4>Superclass of</h4>
  <li><a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="class" href="#KnowledgeBase_c" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="class" href="#Topic_c" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>


</div>
</details>
  
<details class="class" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Conclusion_c">Conclusion</h3>
<a class="class" href="#Conclusion_c">https://w3id.org/contro/arg#Conclusion</a>
</div>

<ul>
  <h4>Equivalent to</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Conclusion_i" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>
<ul>
  <h4>Subclass of</h4>
  <li><a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The statement resulting from an argument. It is supported by a set of premises and justified by the Inference Rule that connects them.</p>


</summary>
<div class="extra">

<ul>
  <h4>In range of</h4>
  <li><a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span></li>
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
  
<details class="class" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Conflict_c">Conflict</h3>
<a class="class" href="#Conflict_c">https://w3id.org/contro/arg#Conflict</a>
</div>

<ul>
  <h4>Subclass of</h4>
  <li><a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="object_property" href="#attacks_op" title="https://w3id.org/contro/arg#attacks">attacks</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">An argument that establishes a conflict relation with another one.</p>


</summary>
<div class="extra">

<ul>
  <h4>Superclass of</h4>
  <li><a class="class" href="#Undercut_c" title="https://w3id.org/contro/arg#Undercut">Undercut</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="class" href="#Undermining_c" title="https://w3id.org/contro/arg#Undermining">Undermining</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>In domain of</h4>
  <li><a class="object_property" href="#attacks_op" title="https://w3id.org/contro/arg#attacks">attacks</a><span class="sup" data-text="op" title="Object Property"></span></li>
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
  <h4>Equivalent to</h4>
  <li><a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span> and <br/><a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> exactly 1 <a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Subclass of</h4>
  <li><a class="object_property" href="https://w3id.org/contro/persp#Attitude" title="https://w3id.org/contro/persp#Attitude">Attitude</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">An argument that draws a conclusion from a set of premises and an Inference Rule and that is susceptible of an attack that targets said Inference Rule.</p>





</div>
  
<details class="class" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="InferenceRule_c">Inference Rule</h3>
<a class="class" href="#InferenceRule_c">https://w3id.org/contro/arg#InferenceRule</a>
</div>

<ul>
  <h4>Equivalent to</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#InferenceRule_i" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span> and <br/><a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span> and <br/><a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">An inference rule is a way of drawing a conclusion from a set of premises.
It can be named and referred to (negatively) in undercut attacks. Together with premises, they are part of the knowledge base of the dialogical agent who constructs the argument.
When applied in an argument, the antecedents of the rule take the role of premises and the consequent that of the conclusion.</p>


</summary>
<div class="extra">


<ul>
<h4>Also defined as</h4>
<li>
<a class="individual" href="#InferenceRule_i" title="https://w3id.org/contro/arg#InferenceRule">Individual</a>
</li>
</ul>

</div>
</details>
  
<details class="class" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="KnowledgeBase_c">Knowledge Base</h3>
<a class="class" href="#KnowledgeBase_c">https://w3id.org/contro/arg#KnowledgeBase</a>
</div>

<ul>
  <h4>Equivalent to</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#KnowledgeBase_i" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>
<ul>
  <h4>Subclass of</h4>
  <li><a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">A knowledge base in an argumentation system is a set containing premises and rules available to an agent to construct arguments.</p>


</summary>
<div class="extra">

<ul>
  <h4>In range of</h4>
  <li><a class="object_property" href="#KnowledgeBase_op" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="op" title="Object Property"></span></li>
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
  
<details class="class" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Literal_c">Literal</h3>
<a class="class" href="#Literal_c">https://w3id.org/contro/arg#Literal</a>
</div>

<ul>
  <h4>Subclass of</h4>
  <li><a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">A propositional literal.</p>


</summary>
<div class="extra">

<ul>
  <h4>Instances</h4>
  <li><a class="individual" href="#A_i" title="https://w3id.org/contro/arg#A">A</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="individual" href="#B_i" title="https://w3id.org/contro/arg#B">B</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="individual" href="#C_i" title="https://w3id.org/contro/arg#C">C</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="individual" href="#D_i" title="https://w3id.org/contro/arg#D">D</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<details class="class" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Premise_c">Premise</h3>
<a class="class" href="#Premise_c">https://w3id.org/contro/arg#Premise</a>
</div>

<ul>
  <h4>Equivalent to</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Premise_i" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>
<ul>
  <h4>Subclass of</h4>
  <li><a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">A statement that supports an argument and that in conjunction with an Inference Rule leads to a conclusion.</p>


</summary>
<div class="extra">

<ul>
  <h4>In range of</h4>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span></li>
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
  <li><a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span> and <br/><a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> exactly 1 <a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Subclass of</h4>
  <li><a class="object_property" href="https://w3id.org/contro/persp#Attitude" title="https://w3id.org/contro/persp#Attitude">Attitude</a><span class="sup" data-text="op" title="Object Property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> min 3 <a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">A rebuttal is a conflict that attacks an argument on its conclusion, providing an alternative one.</p>





</div>
  
<details class="class" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Statement_c">Statement</h3>
<a class="class" href="#Statement_c">https://w3id.org/contro/arg#Statement</a>
</div>

<ul>
  <h4>Equivalent to</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Statement_i" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>
<ul>
  <h4>Subclass of</h4>
  <li><a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">Any kind of proposition expressed or implied by a Dialogical Agent that can be assigned a truth value. They can either be atomic (Literal) or an Inference Rule that connects other statements together.</p>


</summary>
<div class="extra">

<ul>
  <h4>Superclass of</h4>
  <li><a class="class" href="#Conclusion_c" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="class" href="#Literal_c" title="https://w3id.org/contro/arg#Literal">Literal</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="class" href="#Premise_c" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>In range of</h4>
  <li><a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span></li>
  <li><a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span></li>
  <li><a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>
<ul>
  <h4>In domain of</h4>
  <li><a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>
<ul>
  <h4>Disjoint with</h4>
  <li><a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Disjoint union</h4>
  <li><a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="c" title="Class"></span> or <a class="class" href="#Literal_c" title="https://w3id.org/contro/arg#Literal">Literal</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>

<ul>
<h4>Also defined as</h4>
<li>
<a class="individual" href="#Statement_i" title="https://w3id.org/contro/arg#Statement">Individual</a>
</li>
</ul>

</div>
</details>
  
<details class="class" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Topic_c">Topic</h3>
<a class="class" href="#Topic_c">https://w3id.org/contro/arg#Topic</a>
</div>

<ul>
  <h4>Equivalent to</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="sup" data-text="op" title="Object Property"></span> value <a class="individual" href="#Topic_i" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>
<ul>
  <h4>Subclass of</h4>
  <li><a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="sup" data-text="c" title="Class"></span></li>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/d0.owl#Eventuality" title="http://www.ontologydesignpatterns.org/ont/d0.owl#Eventuality">Eventuality</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The eventuality about which an argument expresses an opinion.</p>


</summary>
<div class="extra">

<ul>
  <h4>In range of</h4>
  <li><a class="object_property" href="#Topic_op" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>

<ul>
<h4>Also defined as</h4>
<li>
<a class="object_property" href="#Topic_op" title="https://w3id.org/contro/arg#Topic">Object Property</a>
</li>
<li>
<a class="individual" href="#Topic_i" title="https://w3id.org/contro/arg#Topic">Individual</a>
</li>
</ul>

</div>
</details>
  
<div class="admonition class" markdown>
<div class="admonition-title overview">

<div class="label">
<h3 id="Undercut_c">Undercut</h3>
<a class="class" href="#Undercut_c">https://w3id.org/contro/arg#Undercut</a>
</div>

<ul>
  <h4>Subclass of</h4>
  <li><a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span></li>
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
  <h4>Subclass of</h4>
  <li><a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">An undermining is a conflict that attacks an argument on its premise.</p>





</div>
  

## Object Properties

<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Antecedent_op">Antecedent</h3>
<a class="object_property" href="#Antecedent_op">https://w3id.org/contro/arg#Antecedent</a>
</div>

<ul>
  <h4>Domain</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Range</h4>
  <li><a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The relationship that defines the first half of an hypothetical proposition (Inference Rule).</p>


</summary>
<div class="extra">

<ul>
  <h4>Subproperty of</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is Setting For</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>

<ul>
<h4>Also defined as</h4>
<li>
<a class="individual" href="#Antecedent_i" title="https://w3id.org/contro/arg#Antecedent">Individual</a>
</li>
</ul>

</div>
</details>
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="attackedBy_op">attacked By</h3>
<a class="object_property" href="#attackedBy_op">https://w3id.org/contro/arg#attackedBy</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Inverse of</h4>
  <li><a class="object_property" href="#attacks_op" title="https://w3id.org/contro/arg#attacks">attacks</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>


</div>
</details>
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="attacks_op">attacks</h3>
<a class="object_property" href="#attacks_op">https://w3id.org/contro/arg#attacks</a>
</div>

<ul>
  <h4>Domain</h4>
  <li><a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Range</h4>
  <li><a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The relationship between a Conflict and the argument it targets.</p>


</summary>
<div class="extra">

<ul>
  <h4>Inverse of</h4>
  <li><a class="object_property" href="#attackedBy_op" title="https://w3id.org/contro/arg#attackedBy">attacked By</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>
<ul>
  <h4>Superproperty of chain</h4>
  <li><a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span>)</li>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span>)</li>
</ul>


</div>
</details>
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Author_op">Author</h3>
<a class="object_property" href="#Author_op">https://w3id.org/contro/arg#Author</a>
</div>

<ul>
  <h4>Domain</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Range</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>



</summary>
<div class="extra">

<ul>
  <h4>Subproperty of</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is Setting For</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>
<ul>
  <h4>Superproperty of chain</h4>
  <li><a class="object_property" href="#Author_op" title="https://w3id.org/contro/arg#Author">Author</a><span class="sup" data-text="op" title="Object Property"></span> o <a class="object_property" href="#personaOf_op" title="https://w3id.org/contro/arg#personaOf">persona Of</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>

<ul>
<h4>Also defined as</h4>
<li>
<a class="individual" href="#Author_i" title="https://w3id.org/contro/arg#Author">Individual</a>
</li>
</ul>

</div>
</details>
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Conclusion_op">Conclusion</h3>
<a class="object_property" href="#Conclusion_op">https://w3id.org/contro/arg#Conclusion</a>
</div>

<ul>
  <h4>Domain</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Range</h4>
  <li><a class="class" href="#Conclusion_c" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The statement resulting from an argument. It is supported by a set of premises and justified by the Inference Rule that connects them.</p>


</summary>
<div class="extra">

<ul>
  <h4>Subproperty of</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is Setting For</a><span class="sup" data-text="op" title="Object Property"></span></li>
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
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Consequent_op">Consequent</h3>
<a class="object_property" href="#Consequent_op">https://w3id.org/contro/arg#Consequent</a>
</div>

<ul>
  <h4>Domain</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Range</h4>
  <li><a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The relationship that defines the second half of an hypothetical proposition (Inference Rule).</p>


</summary>
<div class="extra">

<ul>
  <h4>Subproperty of</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is Setting For</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>

<ul>
<h4>Also defined as</h4>
<li>
<a class="individual" href="#Consequent_i" title="https://w3id.org/contro/arg#Consequent">Individual</a>
</li>
</ul>

</div>
</details>
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="contradictedBy_op">contradicted By</h3>
<a class="object_property" href="#contradictedBy_op">https://w3id.org/contro/arg#contradictedBy</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Inverse of</h4>
  <li><a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>


</div>
</details>
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="contradicts_op">contradicts</h3>
<a class="object_property" href="#contradicts_op">https://w3id.org/contro/arg#contradicts</a>
</div>

<ul>
  <h4>Domain</h4>
  <li><a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Range</h4>
  <li><a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The relationship between two opposing statements.</p>


</summary>
<div class="extra">

<ul>
  <h4>Inverse of</h4>
  <li><a class="object_property" href="#contradictedBy_op" title="https://w3id.org/contro/arg#contradictedBy">contradicted By</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>


</div>
</details>
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="KnowledgeBase_op">Knowledge Base</h3>
<a class="object_property" href="#KnowledgeBase_op">https://w3id.org/contro/arg#KnowledgeBase</a>
</div>

<ul>
  <h4>Domain</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Range</h4>
  <li><a class="class" href="#KnowledgeBase_c" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">A knowledge base in an argumentation system is a set containing premises and rules available to an agent to construct arguments.</p>


</summary>
<div class="extra">

<ul>
  <h4>Subproperty of</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is Setting For</a><span class="sup" data-text="op" title="Object Property"></span></li>
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
  
<div class="admonition object_property" markdown>
<div class="admonition-title overview">

<div class="label">
<h3 id="personaOf_op">persona Of</h3>
<a class="object_property" href="#personaOf_op">https://w3id.org/contro/arg#personaOf</a>
</div>

<ul>
  <h4>Domain</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Range</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>






</div>
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Premise_op">Premise</h3>
<a class="object_property" href="#Premise_op">https://w3id.org/contro/arg#Premise</a>
</div>

<ul>
  <h4>Domain</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Range</h4>
  <li><a class="class" href="#Premise_c" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">A statement that supports an argument and that in conjunction with an Inference Rule leads to a conclusion.</p>


</summary>
<div class="extra">

<ul>
  <h4>Subproperty of</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is Setting For</a><span class="sup" data-text="op" title="Object Property"></span></li>
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
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="supportedBy_op">supported By</h3>
<a class="object_property" href="#supportedBy_op">https://w3id.org/contro/arg#supportedBy</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Inverse of</h4>
  <li><a class="object_property" href="#supports_op" title="https://w3id.org/contro/arg#supports">supports</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>


</div>
</details>
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="supports_op">supports</h3>
<a class="object_property" href="#supports_op">https://w3id.org/contro/arg#supports</a>
</div>

</div>

<p class="description">The relationship between two arguments in which the first's conclusion acts as the second's premise.</p>


</summary>
<div class="extra">

<ul>
  <h4>Inverse of</h4>
  <li><a class="object_property" href="#supportedBy_op" title="https://w3id.org/contro/arg#supportedBy">supported By</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>
<ul>
  <h4>Superproperty of chain</h4>
  <li><a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> o inverse(<a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span>)</li>
</ul>


</div>
</details>
  
<details class="object_property" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Topic_op">Topic</h3>
<a class="object_property" href="#Topic_op">https://w3id.org/contro/arg#Topic</a>
</div>

<ul>
  <h4>Domain</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation">Situation</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
<ul>
  <h4>Range</h4>
  <li><a class="class" href="#Topic_c" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The eventuality about which an argument expresses an opinion.</p>


</summary>
<div class="extra">

<ul>
  <h4>Subproperty of</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#isSettingFor">is Setting For</a><span class="sup" data-text="op" title="Object Property"></span></li>
</ul>

<ul>
<h4>Also defined as</h4>
<li>
<a class="class" href="#Topic_c" title="https://w3id.org/contro/arg#Topic">Class</a>
</li>
<li>
<a class="individual" href="#Topic_i" title="https://w3id.org/contro/arg#Topic">Individual</a>
</li>
</ul>

</div>
</details>
  





## Individuals

<div class="admonition individual" markdown>
<div class="admonition-title overview">

<div class="label">
<h3 id="A_i">A</h3>
<a class="individual" href="#A_i">https://w3id.org/contro/arg#A</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="#Literal_c" title="https://w3id.org/contro/arg#Literal">Literal</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>






</div>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="A_and_C__implies_not_B_i">A_and_C__implies_not_B</h3>
<a class="individual" href="#A_and_C__implies_not_B_i">https://w3id.org/contro/arg#A_and_C__implies_not_B</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#A_i" title="https://w3id.org/contro/arg#A">A</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#C_i" title="https://w3id.org/contro/arg#C">C</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#not_B_i" title="https://w3id.org/contro/arg#not_B">not_B</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="A_implies_B_i">A_implies_B</h3>
<a class="individual" href="#A_implies_B_i">https://w3id.org/contro/arg#A_implies_B</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#A_i" title="https://w3id.org/contro/arg#A">A</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#B_i" title="https://w3id.org/contro/arg#B">B</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="alias_i">alias</h3>
<a class="individual" href="#alias_i">https://w3id.org/contro/arg#alias</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#personaOf_op" title="https://w3id.org/contro/arg#personaOf">persona Of</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#secret_opponent_i" title="https://w3id.org/contro/arg#secret_opponent">secret_opponent</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Antecedent_i">Antecedent</h3>
<a class="individual" href="#Antecedent_i">https://w3id.org/contro/arg#Antecedent</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The relationship that defines the first half of an hypothetical proposition (Inference Rule).</p>


</summary>
<div class="extra">


<ul>
<h4>Also defined as</h4>
<li>
<a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Object Property</a>
</li>
</ul>

</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Argument_i">Argument</h3>
<a class="individual" href="#Argument_i">https://w3id.org/contro/arg#Argument</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">An argument is defined relative to an argumentation theory and a knowledge base. Its premises are the formulas and inference rule from the knowledge base, its conclusion is the formula inferred from the premises through the application of said inference rule.</p>


</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Author_i" title="https://w3id.org/contro/arg#Author">Author</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Conclusion_i" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#KnowledgeBase_i" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Premise_i" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Topic_i" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>

<ul>
<h4>Also defined as</h4>
<li>
<a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Class</a>
</li>
</ul>

</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Author_i">Author</h3>
<a class="individual" href="#Author_i">https://w3id.org/contro/arg#Author</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>



</summary>
<div class="extra">


<ul>
<h4>Also defined as</h4>
<li>
<a class="object_property" href="#Author_op" title="https://w3id.org/contro/arg#Author">Object Property</a>
</li>
</ul>

</div>
</details>
  
<div class="admonition individual" markdown>
<div class="admonition-title overview">

<div class="label">
<h3 id="B_i">B</h3>
<a class="individual" href="#B_i">https://w3id.org/contro/arg#B</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="#Literal_c" title="https://w3id.org/contro/arg#Literal">Literal</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>






</div>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="B_implies_D_i">B_implies_D</h3>
<a class="individual" href="#B_implies_D_i">https://w3id.org/contro/arg#B_implies_D</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#B_i" title="https://w3id.org/contro/arg#B">B</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#D_i" title="https://w3id.org/contro/arg#D">D</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<div class="admonition individual" markdown>
<div class="admonition-title overview">

<div class="label">
<h3 id="C_i">C</h3>
<a class="individual" href="#C_i">https://w3id.org/contro/arg#C</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="#Literal_c" title="https://w3id.org/contro/arg#Literal">Literal</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>






</div>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Conclusion_i">Conclusion</h3>
<a class="individual" href="#Conclusion_i">https://w3id.org/contro/arg#Conclusion</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The statement resulting from an argument. It is supported by a set of premises and justified by the Inference Rule that connects them.</p>


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
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Consequent_i">Consequent</h3>
<a class="individual" href="#Consequent_i">https://w3id.org/contro/arg#Consequent</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The relationship that defines the second half of an hypothetical proposition (Inference Rule).</p>


</summary>
<div class="extra">


<ul>
<h4>Also defined as</h4>
<li>
<a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Object Property</a>
</li>
</ul>

</div>
</details>
  
<div class="admonition individual" markdown>
<div class="admonition-title overview">

<div class="label">
<h3 id="D_i">D</h3>
<a class="individual" href="#D_i">https://w3id.org/contro/arg#D</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="#Literal_c" title="https://w3id.org/contro/arg#Literal">Literal</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>






</div>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="defeasible_inference_i">defeasible_inference</h3>
<a class="individual" href="#defeasible_inference_i">https://w3id.org/contro/arg#defeasible_inference</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#Author_op" title="https://w3id.org/contro/arg#Author">Author</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#alias_i" title="https://w3id.org/contro/arg#alias">alias</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#B_i" title="https://w3id.org/contro/arg#B">B</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#A_i" title="https://w3id.org/contro/arg#A">A</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Topic_op" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#topic_1_i" title="https://w3id.org/contro/arg#topic_1">topic_1</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="dependant_inference_i">dependant_inference</h3>
<a class="individual" href="#dependant_inference_i">https://w3id.org/contro/arg#dependant_inference</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#D_i" title="https://w3id.org/contro/arg#D">D</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#B_i" title="https://w3id.org/contro/arg#B">B</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="dependant_undermining_i">dependant_undermining</h3>
<a class="individual" href="#dependant_undermining_i">https://w3id.org/contro/arg#dependant_undermining</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#B_implies_D_i" title="https://w3id.org/contro/arg#B_implies_D">B_implies_D</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#not_B_i" title="https://w3id.org/contro/arg#not_B">not_B</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="InferenceRule_i">Inference Rule</h3>
<a class="individual" href="#InferenceRule_i">https://w3id.org/contro/arg#InferenceRule</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">An inference rule is a way of drawing a conclusion from a set of premises.
It can be named and referred to (negatively) in undercut attacks. Together with premises, they are part of the knowledge base of the dialogical agent who constructs the argument.
When applied in an argument, the antecedents of the rule take the role of premises and the consequent that of the conclusion.</p>


</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Antecedent_i" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#Consequent_i" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>

<ul>
<h4>Also defined as</h4>
<li>
<a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Class</a>
</li>
</ul>

</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="KnowledgeBase_i">Knowledge Base</h3>
<a class="individual" href="#KnowledgeBase_i">https://w3id.org/contro/arg#KnowledgeBase</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">A knowledge base in an argumentation system is a set containing premises and rules available to an agent to construct arguments.</p>


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
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="not__A_implies_B_i">not__A_implies_B</h3>
<a class="individual" href="#not__A_implies_B_i">https://w3id.org/contro/arg#not__A_implies_B</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#A_implies_B_i" title="https://w3id.org/contro/arg#A_implies_B">A_implies_B</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="not_A_i">not_A</h3>
<a class="individual" href="#not_A_i">https://w3id.org/contro/arg#not_A</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#A_i" title="https://w3id.org/contro/arg#A">A</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="not_B_i">not_B</h3>
<a class="individual" href="#not_B_i">https://w3id.org/contro/arg#not_B</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#B_i" title="https://w3id.org/contro/arg#B">B</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Premise_i">Premise</h3>
<a class="individual" href="#Premise_i">https://w3id.org/contro/arg#Premise</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">A statement that supports an argument and that in conjunction with an Inference Rule leads to a conclusion.</p>


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
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="rebuttal_i">rebuttal</h3>
<a class="individual" href="#rebuttal_i">https://w3id.org/contro/arg#rebuttal</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#not_B_i" title="https://w3id.org/contro/arg#not_B">not_B</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#A_i" title="https://w3id.org/contro/arg#A">A</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#C_i" title="https://w3id.org/contro/arg#C">C</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<div class="admonition individual" markdown>
<div class="admonition-title overview">

<div class="label">
<h3 id="secret_opponent_i">secret_opponent</h3>
<a class="individual" href="#secret_opponent_i">https://w3id.org/contro/arg#secret_opponent</a>
</div>

</div>






</div>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Statement_i">Statement</h3>
<a class="individual" href="#Statement_i">https://w3id.org/contro/arg#Statement</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">Any kind of proposition expressed or implied by a Dialogical Agent that can be assigned a truth value. They can either be atomic (Literal) or an Inference Rule that connects other statements together.</p>


</summary>
<div class="extra">


<ul>
<h4>Also defined as</h4>
<li>
<a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Class</a>
</li>
</ul>

</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="Topic_i">Topic</h3>
<a class="individual" href="#Topic_i">https://w3id.org/contro/arg#Topic</a>
</div>

<ul>
  <h4>Class</h4>
  <li><a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="sup" data-text="c" title="Class"></span></li>
</ul>
</div>

<p class="description">The eventuality about which an argument expresses an opinion.</p>


</summary>
<div class="extra">


<ul>
<h4>Also defined as</h4>
<li>
<a class="object_property" href="#Topic_op" title="https://w3id.org/contro/arg#Topic">Object Property</a>
</li>
<li>
<a class="class" href="#Topic_c" title="https://w3id.org/contro/arg#Topic">Class</a>
</li>
</ul>

</div>
</details>
  
<div class="admonition individual" markdown>
<div class="admonition-title overview">

<div class="label">
<h3 id="topic_1_i">topic_1</h3>
<a class="individual" href="#topic_1_i">https://w3id.org/contro/arg#topic_1</a>
</div>

</div>






</div>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="undercut_i">undercut</h3>
<a class="individual" href="#undercut_i">https://w3id.org/contro/arg#undercut</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#A_i" title="https://w3id.org/contro/arg#A">A</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#not__A_implies_B_i" title="https://w3id.org/contro/arg#not__A_implies_B">not__A_implies_B</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  
<details class="individual" markdown>
<summary>
<div class="overview">

<div class="label">
<h3 id="undermining_i">undermining</h3>
<a class="individual" href="#undermining_i">https://w3id.org/contro/arg#undermining</a>
</div>

</div>



</summary>
<div class="extra">

<ul>
  <h4>Assertions</h4>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#A_implies_B_i" title="https://w3id.org/contro/arg#A_implies_B">A_implies_B</a><span class="sup" data-text="i" title="Individual"></span></li>
  <li><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span> <a class="individual" href="#not_A_i" title="https://w3id.org/contro/arg#not_A">not_A</a><span class="sup" data-text="i" title="Individual"></span></li>
</ul>


</div>
</details>
  

## Rules

<div class="admonition rule" markdown>
<div class="admonition-title overview">

<div class="label">
<h3 id="S1">S1</h3>
</div>

</div>

<p class="description">An argumentation that concludes B from A has the implicit premise that there exists an implication from A to B</p>

<p><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span>(?a, ?p) ∧ <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="sup" data-text="op" title="Object Property"></span>(?a, ?c) ∧ <a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="sup" data-text="op" title="Object Property"></span>(?i, ?p) ∧ <a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="sup" data-text="op" title="Object Property"></span>(?i, ?c) → <a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span>(?a, ?i)</p>




</div>
  
<div class="admonition rule" markdown>
<div class="admonition-title overview">

<div class="label">
<h3 id="S2">S2</h3>
</div>

</div>

<p class="description">An Undercut is a conflict that negates the implication of the argumentation it attacks.</p>

<p><a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="sup" data-text="c" title="Class"></span>(?p) ∧ <a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span>(?a, ?not_p) ∧ <a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span>(?a) ∧ <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span>(?not_p, ?p) → <a class="class" href="#Undercut_c" title="https://w3id.org/contro/arg#Undercut">Undercut</a><span class="sup" data-text="c" title="Class"></span>(?a)</p>




</div>
  
<div class="admonition rule" markdown>
<div class="admonition-title overview">

<div class="label">
<h3 id="S3">S3</h3>
</div>

</div>

<p class="description">An Undermining is a conflict that negates an atomic statement that is a premise of the argumentation it attacks.</p>

<p><a class="class" href="#Literal_c" title="https://w3id.org/contro/arg#Literal">Literal</a><span class="sup" data-text="c" title="Class"></span>(?p) ∧ <a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="sup" data-text="op" title="Object Property"></span>(?a, ?not_p) ∧ <a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="sup" data-text="c" title="Class"></span>(?a) ∧ <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="sup" data-text="op" title="Object Property"></span>(?not_p, ?p) → <a class="class" href="#Undermining_c" title="https://w3id.org/contro/arg#Undermining">Undermining</a><span class="sup" data-text="c" title="Class"></span>(?a)</p>




</div>
  


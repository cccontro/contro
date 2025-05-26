<h1>The argumentation ontology</h1>

## Overview

## Classes

<details class="class" markdown>

<summary>
<div class="overview">
<div class="label">
<h3 id="Argument_c">Argument</h3>
<a class="class" href="#Argument_c">https://w3id.org/contro/arg#Argument</a>
</div>

<dl>
<dt>Equivalent to</dt>
<dd>
<a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies">satisfies</a><span class="superscript" data-text="op" title="Object property"></span>
value
<a class="individual" href="#Argument_i" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="superscript" data-text="i" title="Individual"></span>
</dd>
</dl>

<dl>
<dt>Subclass of</dt>
<dd><a class="class" href="#ArgumentationTheorySituation_c" title="https://w3id.org/contro/arg#ArgumentationTheorySituation">Argumentation Theory Situation</a><span class="superscript" data-text="c" title="Class"></span></dd>
<dd><a class="object_property" href="#Author_op" title="https://w3id.org/contro/arg#Author">Author</a><span class="superscript" data-text="op" title="Object property"></span> some <a class="class" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent">Agent</a><span class="superscript" data-text="c" title="Class"></span></dd>
<dd><a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="superscript" data-text="op" title="Object property"></span> max 1 <a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="superscript" data-text="c" title="Class"></span></dd>
<dd><a class="object_property" href="#KnowledgeBase_op" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="superscript" data-text="op" title="Object property"></span> min 0 <a class="class" href="#Situation_c" title="https://w3id.org/contro/arg#Situation">Situation</a><span class="superscript" data-text="c" title="Class"></span></dd>
<dd><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="superscript" data-text="op" title="Object property"></span> some <a class="class" href="#InferenceRule_c" title="https://w3id.org/contro/arg#InferenceRule">Inference Rule</a><span class="superscript" data-text="c" title="Class"></span></dd>
<dd><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="superscript" data-text="op" title="Object property"></span> some <a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="superscript" data-text="c" title="Class"></span></dd>
<dd><a class="object_property" href="#Topic_op" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="superscript" data-text="op" title="Object property"></span> some <a class="class" href="#Situation_c" title="https://w3id.org/contro/arg#Situation">Situation</a><span class="superscript" data-text="c" title="Class"></span></dd>
</dl>
</div>

<p class="description">
An argument is defined relative to an argumentation theory and a knowledge base. Its premises are the formulas and inference rule from the knowledge base, its conclusion is the formula inferred from the premises through the application of said inference rule.
</p>

</summary>

<div class="extra">

<dl>
<dt>Superclass of</dt>
<dd><a class="class" href="#Conflict_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="superscript" data-text="c" title="Class"></span></dd>
</dl>

<dl>
<dt>In range of</dt>
<dd><a class="object_property" href="#attacks_op" title="https://w3id.org/contro/arg#attacks">attacks</a><span class="superscript" data-text="op" title="Object property"></span></dd>
</dl>

<dl>
<dt>Disjoint with</dt>
<dd><a class="class" href="#Statement_c" title="https://w3id.org/contro/arg#Statement">Statement</a><span class="superscript" data-text="c" title="Class"></span></dd>
</dl>

<dl>
<dt>Also defined as</dt>
<dd><a class="individual" href="#Argument_i" title="https://w3id.org/contro/arg#Argument">Individual</a></dd>
</dl>

</div>
</details>


## Object properties

<details class="object_property" markdown>

<summary>
<div class="overview">
<div class="label">
<h3 id="attacks_op">attacks</h3>
<a class="object_property" href="#attacks_op">https://w3id.org/contro/arg#attacks</a>
</div>

<dl>
<dt>Domain</dt>
<dd><a class="class" href="#Confilct_c" title="https://w3id.org/contro/arg#Conflict">Conflict</a><span class="superscript" data-text="c" title="Class"></span></dd>
</dl>

<dl>
<dt>Range</dt>
<dd><a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Argument</a><span class="superscript" data-text="c" title="Class"></span></dd>
</dl>
</div>

<p class="description">
The relationship between a Conflict and the argument it targets.
</p>

</summary>

<div class="extra">

<dl>
<dt>Inverse of</dt>
<dd><a class="object_property" href="#attackedBy_op" title="https://w3id.org/contro/arg#attackedBy">attacked by</a><span class="superscript" data-text="op" title="Object property"></span></dd>
</dl>

<dl>
<dt>Sub-property chains</dt>
<dd><a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="superscript" data-text="op" title="Object property"></span> o <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="superscript" data-text="op" title="Object property"></span> o inverse (<a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="superscript" data-text="op" title="Object property"></span> )</dd>
<dd><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="superscript" data-text="op" title="Object property"></span> o <a class="object_property" href="#contradicts_op" title="https://w3id.org/contro/arg#contradicts">contradicts</a><span class="superscript" data-text="op" title="Object property"></span> o inverse (<a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="superscript" data-text="op" title="Object property"></span> )</dd>
</dl>

<dl>
<dt>Also defined as</dt>
<dd><a class="individual" href="#Argument_i" title="https://w3id.org/contro/arg#Argument">Individual</a></dd>
</dl>

</div>

</details>

## Individuals

<details class="individual" markdown>

<summary>
<div class="overview">
<div class="label">
<h3 id="Argument_i">Argument</h3>
<a class="individual" href="#Argument_i">https://w3id.org/contro/arg#Argument</a>
</div>

<dl>
<dt>Class</dt>
<dd><a class="class" href="#http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description">Description</a><span class="superscript" data-text="c" title="Class"></span></dd>
</dl>
</div>

<p class="description">
An argument is defined relative to an argumentation theory and a knowledge base. Its premises are the formulas and inference rule from the knowledge base, its conclusion is the formula inferred from the premises through the application of said inference rule.
</p>

</summary>

<div class="extra">

<dl>
<dt>Assertions</dt>
<dd><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="superscript" data-text="op" title="Object property"></span> <a class="individual" href="#Author_i" title="https://w3id.org/contro/arg#Author">Author</a><span class="superscript" data-text="i" title="Individual"></span></dd>
<dd><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="superscript" data-text="op" title="Object property"></span> <a class="individual" href="#Conclusion_i" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="superscript" data-text="i" title="Individual"></span></dd>
<dd><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="superscript" data-text="op" title="Object property"></span> <a class="individual" href="#KnowledgeBase_i" title="https://w3id.org/contro/arg#KnowledgeBase">Knowledge Base</a><span class="superscript" data-text="i" title="Individual"></span></dd>
<dd><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="superscript" data-text="op" title="Object property"></span> <a class="individual" href="#Premise_i" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="superscript" data-text="i" title="Individual"></span></dd>
<dd><a class="object_property" href="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent" title="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent">has Component</a><span class="superscript" data-text="op" title="Object property"></span> <a class="individual" href="#Topic_i" title="https://w3id.org/contro/arg#Topic">Topic</a><span class="superscript" data-text="i" title="Individual"></span></dd>
</dl>

<dl>
<dt>Also defined as</dt>
<dd><a class="class" href="#Argument_c" title="https://w3id.org/contro/arg#Argument">Class</a></dd>
</dl>

</div>

</details>

## SWRL rules

<div class="admonition rule" markdown>

<div class="admonition-title overview">
<div class="label">
<h3 id="R1">R1</h3>
</div>
</div>

<p class="description">An argument that concludes B from A has the implicit premise that there exists an implication from A to B.</p>

<p><a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="superscript" data-text="op" title="Object property"></span>(?a, ?p) ∧ <a class="object_property" href="#Conclusion_op" title="https://w3id.org/contro/arg#Conclusion">Conclusion</a><span class="superscript" data-text="op" title="Object property"></span>(?a, ?c) ∧ <a class="object_property" href="#Antecedent_op" title="https://w3id.org/contro/arg#Antecedent">Antecedent</a><span class="superscript" data-text="op" title="Object property"></span>(?i, ?p) ∧ <a class="object_property" href="#Consequent_op" title="https://w3id.org/contro/arg#Consequent">Consequent</a><span class="superscript" data-text="op" title="Object property"></span>(?i, ?c) → <a class="object_property" href="#Premise_op" title="https://w3id.org/contro/arg#Premise">Premise</a><span class="superscript" data-text="op" title="Object property"></span>(?a, ?i)</p>

</div>
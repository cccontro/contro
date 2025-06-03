---
description:
subtitle: Our design choices
icon: octicons/ai-model-16
---

In engaging with reality, a subject must inevitably conceptualize it, adopting a viewpoint that reflects their subjectivity. Cognitive linguistics argues that such perspectivization process underlies the production of meaning and entails authorial responsibility in discourse: a viewpoint is the cognitive mechanism by which a speaker (or conceptualizer) *construes* an event or situation [@Verhagen2007].

At the core of **cognitive perspectivization** is the subject actively construing a perceived, evaluated, negated, or inferred situation. Because this process is inherently subjective, the same occurrence can be conceptualized in multiple, sometimes conflicting ways. This contrastive dimension becomes especially salient in argumentative contexts.

We therefore treat argumentation as a special case of perspectivization, governed by specific logical constraints. Riteniamo che sia significativo rendere i due modelli compatibili perché...hanno focus complementari: uno sull'estrazione dalla knowledge base di premsse, la costruzione di nuove conclusioni e il conflitto tra di loro, l'altra sulla composizionalità tra il cut e l'eventuality.

## Methodology

Building an ontology is a complex operation since it is intended to be set in context. It is necessary to understand how to reuse or repurpose pre-existing ontologies and translate non-ontological modeling and nonformal resources into description logic.
We followed NeOn methodology [@Suárez-Figueroa2012].
Mixed scenario of non-ontological resource re-enegeering, and reuse of ontology design patterns (ODPs) and ontological resources.

1. Requirement specification (competency questions CQs)
2. Selection of non-ontological resources and reverse engeneering
3. Ontology selection for reuse and restructuring
4. Alignment
4. Conceptualization
5. Formalization
6. Implementation

## Perspectivisation

!!! info inline end "Eventuality"
    
    In the DOLCE foundational ontology, “eventuality” is an umbrella term encompassing events, activities, event types, and situations (configurations that provide a setting for multiple entities) used to abstract from formal distinctions among them.

The *Perspectivisation Ontology Design Pattern* (ODP), introduced in [@Gangemi2022], models the conceptual "cuts" a subject makes on an eventuality through the lenses (conscious or unconscious) available to them. Just as a filmmaker frames reality through a camera lens, a subject construes an eventuality through their own preconceptions, beliefs and values. The result is a **composition** of the eventuality and the conceptualiser’s lens: a cut that is conveyed in the subject’s expressions and may conflict with representations produced by other agents.

This perspectivisation situation is modeled as an *n-ary relation* that links the conceptualiser, the eventuality, the background knowledge from which the eventuality is extracted, the lens through which it is construed, the resulting cut, and the conceptualiser's attitude toward that cut. Apart from the agent who has the role of conceptualiser, all the components of the n-ary relation are also modeled as situations, that is, as further unspecified n-ary relations.

<!-- Come non citare poi grandi campioni come l'Agent e l'Attitude che rompon di brutto i coglioni (leggi che metrica sto periodo) -->

<div class="mermaid" markdown>
<figcaption>Perspectivisation Model</figcaption>
![Diagram of Perspectivisation Ontology](assets/images/Perspectivisation.svg)
</div>

## Argumentation

Abbiamo construtio arugmentation partendo dalle aspic categories prendendo in cosiderazione la struttura di Perspectivisation come reference model. La formalizzazione di argumentation mira ad essere integrabile con pwrspectivisation (in COntr0). 
Il nostro logical language è costutuito da Statements/formulas che possono assumere il ruolo di premesse e conclusioni. 

### Adapting ASPIC^+^ structures
Since our focus is capturing the notion of argumentation in real-world contexts, we considered the features of the framework that represent defeasible reasoning, leaving aside those dedicated to strictly deductive reasoning. Moreover, since our main objective was to represent the structure of argumentation (to understand the differences in styles of argumentation, not to determine a winner), we did not implement the preference mechanism to establish the winner argument. This could be integrated in the future.

ASPIC+ combines deductive and defeasible argumentation. Only used defeasilbe rules and assumptions. No, not made the distinction.
Simplified argumentation theory as composded of argumentation system and knowledge base by including everything in knowledge base.

Single argument and not chain applications. Is the conclusion or the argument itself that becomes the premise of a new argument?

ASPIC+ does not model temporal acceptance or staged assumption revision. So:
- The act of temporarily granting A and then later asserting ¬A leads to a conflict in the argument graph: both A and ¬A appear in different arguments.
- The resulting abstract argumentation framework may be inconsistent or unstable, depending on the semantics used (e.g., no admissible extension includes both).

### Limitations of OWL DL

- OWA:
    - Conceded arguments are equated with the not-yet-attacked arguments.
    - it is necessary to explicitly mark up atomic propositions to distinguish them from statements that represent inference rules.
    - The reasoner cannot make inferences about non-explicit negations.

- Monotonic

### Argument construction
2 ways:
1. Arg e inf rule have the same antecedents/premises and consequent/conclusion -> appartenenza di inf rule ad argument inferred
2. Inf rule assigned to argument -> premises and conclusion of argument inferred from inf rule

<div class="mermaid" markdown>
<figcaption>Argumentation Model</figcaption>
![Diagram of Argumentation Ontology](assets/images/Argumentation.svg)
</div>

### Conflict schemes

## CONTRO

| Persp             | ⊇ | Arg                            |
|-------------------|:-:|--------------------------------|
| Perspectivisation |   | Argument                       |
| Lens              |   | Premise ∪ Inference Rule       |
| Cut               |   | Conclusion                     |
| Background        |   | Knowledge Base                 |
| Attitude          |   | Acceptance Attitude            |

## Descriptions and Situations
We modelled as roles the structures that we did not wanted to describe but we drew from DOLCE. (eventuality as a topic, an agent as a dialogical agent) vs descriptions, which are the theoretical equivalent of the situation configurations we described.
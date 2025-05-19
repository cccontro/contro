---
description:
subtitle: Our design choices
icon: octicons/ai-model-16
---

## Methodology

We followed NeOn methodology [@Suárez-Figueroa2012].
Mixed scenario of non-ontological resource re-enegeering, and reuse of ontology design patterns (ODPs) and ontological resources.

1. Requirement specification (competency questions CQs)
2. Selection of non-ontological resources and reverse engeneering
3. Ontology selection for reuse and restructuring
4. Alignment
4. Conceptualization
5. Formalization
6. Implementation

These steps need to be taken iteratively as in our case we were adapting a non-monotonic and closed-world framework to a monotonic and open-world language (OWL).

## Limitations of OWL DL

- OWA
- Montonic

## ASPIC^+^
Since our focus is capturing the notion of argumentation in real-world contexts, we considered the features of the framework that represent defeasible reasoning, leaving aside those dedicated to strictly deductive reasoning. Moreover, since our main objective was to represent the structure of argumentation, we did not implement the preference mechanism to establish the winner argument. This could be integrated in the future.

## Adapting pespectivation framework to argumentation

- Explicit Lens
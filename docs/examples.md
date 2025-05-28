---
description:
subtitle: CONTRO in action
icon: bootstrap/chat-quote-fill
extra_css:
  - assets/stylesheets/tei.css
---

<h1>Examples</h1>

CONTRO's aim is to extract opinions—both implicit and explicit—as they emerge within dialectical discourse through its structure. In this section, we demonstrate how illuminating this formal interpretation can be, using the first point of contention between Caro and Castelvetro as a case study.

We begin by reconstructing the arguments directly from the text. Then, we show how these arguments are formalized in the ontology—both from the diachronic perspective of argumentative progression and the synchronic perspective of cognitive perspectivization. If you prefer to skip the textual excerpts, you can go directly to the [next section](#from-tree-to-graph).

## Argument analysis in text

Applying argumentation theory to textual analysis reveals latent argumentative structures that are often obscured by rhetorical strategies and implicatures. It enables us to:

- Reconstruct implicit premises and conclusions;
- Identify the opponent's assertions that are the target of critique;
- Classify the type of attack (on premises, implications, or conclusions);
- Break down complex arguments into atomic ones, each with at most one conclusion and one attack type.

For instance, an argument that **negates a premise** and **proposes an alternative conclusion** is, in fact, composed of two sub-arguments. The first is an attack on the opponent’s argument that relies on the (positive form of the) negated premise. Depending on whether the negated premise is an atomic proposition or a rule of inference, this attack may take the form of undermining or undercutting, respectively. Notably, this first sub-argument lacks a conclusion: it is purely destructive.

The second sub-argument introduces a rebuttal (or distinction) that supports a contradictory conclusion. To do so, it must introduce an additional, often implicit, premise that justifies the new conclusion in light of the premises that remain acceptable. This structure exemplifies **non-monotonic reasoning**: attacking the premises alone is not enough to reach a different conclusion—it merely invalidates the opponent’s. To move from *pars destruens* to *pars construens*, further ontological commitments are required to support an alternative vision of the issue at stake.

This pattern is at play in [Caro's response](#predellas-resentment) (under the pseudonym Predella) to the first point of Castelvetro's critique.

/// tab | English
--8<-- "tei/Apologia-TEI.md"
///

/// tab | Italian
--8<-- "tei/Apologia-TEI-it.md"
///

## From tree to graph

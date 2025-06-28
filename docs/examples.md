---
description:
subtitle: CONTRO in action
icon: bootstrap/chat-quote-fill
extra_css:
  - assets/stylesheets/tei.css
toc_depth: 3
---

<h1>Examples</h1>

CONTRO’s aim is to extract opinions—both implicit and explicit—as they emerge within dialectical discourse through its structure. In this section, we demonstrate how illuminating this formal interpretation can be, using the first point of contention between Caro and Castelvetro as a case study.

We begin by reconstructing the arguments directly from the text. Then, we show how these arguments are formalized in the ontology, both as arguments and as persepctives. If you prefer to skip the textual excerpts, you can go directly to the [last section](#from-tree-to-graph). In the project’s repository you can consult the annotated texts in [`Apologia-TEI.xml`](https://github.com/cccontro/contro/blob/main/tei/Apologia-TEI.xml) and [`Ragione-TEI.xml`](https://github.com/cccontro/contro/blob/main/tei/Ragione-TEI.xml).

## Argument analysis in text

Applying argumentation theory to textual analysis reveals latent argumentative structures that are often obscured by rhetorical strategies and implicatures. It enables us to:

- Reconstruct implicit premises and conclusions;
- Identify the opponent’s assertions that are the target of critique;
- Classify the type of attack (on premises, inference rules, or conclusions);
- Break down complex arguments into atomic ones, each with at most one conclusion and one attack target.

For instance, an argument that **negates a premise** and **proposes an alternative conclusion** is, in fact, composed of two sub-arguments. The first is an undermining on the opponent’s argument that relies on the (positive form of the) negated premise.  The second sub-argument introduces a rebuttal (or distinction) that supports a contradictory conclusion. To do so, it should introduce an additional, often implicit, premise that justifies the new conclusion in light of the premises that remain acceptable. This structure exemplifies **non-monotonic reasoning**: attacking the premises alone is not enough to reach a different conclusion—it merely invalidates the opponent’s. To move from *pars destruens* to *pars construens*, further ontological commitments are required to support an alternative vision of the issue at stake.

This pattern is at play in [Caro’s response](#predellas-resentment) (under the pseudonym Predella) to the first point of Castelvetro’s critique. Our formalization of this reply also illustrates how Walton’s [scheme from expert opinion](background.md#contextual-approaches) is abstracted within the ASPIC^+^ framework: critical questions targeting the credibility of the expert or the validity of their claims function as undercutters, while the appeal to alternative expert opinions gives rise to a rebuttal [@Prakken2011; pp. 14--15]. Caro employs both moves, consistent with his rhetorical method of overwhelming the opponent through a multiplicity of attacks.

/// tab | English
--8<-- "tei/Apologia-TEI.md"
///

/// tab | Italian
--8<-- "tei/Apologia-TEI-it.md"
///


/// tab | English
    new: true
--8<-- "tei/Ragione-TEI.md"
///

/// tab | Italian
--8<-- "tei/Ragione-TEI-it.md"
///


## From tree to graph

Ignore conditionals and flatten *reductio ad abusrdum* into a premise.


<div class="strawpoll-embed" id="strawpoll_3RnYXmzwzye" style="height: 480px; max-width: 640px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;"><iframe id="strawpoll_iframe_3RnYXmzwzye" src="https://strawpoll.com/embed/3RnYXmzwzye" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe></div>

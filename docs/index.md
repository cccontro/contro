---
hide:
  - navigation
description:
subtitle: About the project
icon: material/earth
template: hero.html
---

<div id="hero-bg" aria-hidden="true" role="presentation" data-search-exclude markdown="span">
![Calligram of Castelvetro](assets/images/Castelvetro.svg)
![Calligram of Caro](assets/images/Caro.svg)
</div>

<section class="hero">
  <h1>A <span class="emph">Contro</span>versy-Oriented Model of Dialectical Perspectives</h1>
  <div class="md-button" aria-hidden="true" role="presentation" onclick='document.getElementById("quotes").scrollIntoView({ block: "center", behavior: "smooth"})' data-search-exclude>Let's argue</div>
</section>

<section id="quotes" markdown>

<div class="grid cards no-border" markdown hidden>

- > Not even this is left to words, namely, that at any rate they express the mind of the speaker, since a speaker may indeed not know the things about which he speaks.

    ==Augustine of Hippo, *De Magistro*, XIII 42==

- > The reasons (motives) people may have for holding a&nbsp;belief are not always the same as the reasons (grounds) they will offer and accept in defense of a&nbsp;claim.

    ==Frans H. van Eemeren, *Reconstructing Argumentative Discourse*, p. 12==

</div>
</section>

<section id="distill" markdown>

<div class="grid cards no-border" markdown hidden>

- # How to distill an opinion

    Our project aims to formalize how personal perspectives are externalized through argumentation in dialectical contexts. What we are interested in is the *shape* of an argument: when discourse is reconstructed in terms of argumentation structures, the communicative intent of the agents involved emerges with greater clarity.

- ![Opinion distiller](assets/images/distiller.svg)

</div>

</section>

<section id="questions" markdown>
Given a dialogical agent, we can ask the following questions:

<div class="grid cards" markdown hidden>
- How is their argumentative style characterized?
- What kinds of attacks do they tend to favor?
- What reasons do they put forward during argumentation?
- What reasons are implicit in their arguments?
- How are these reasons reflected in their view of the issue at stake?
</div>

</section>

<section id="overview" markdown>

# CONTRO is designed to answer

<div class="grid cards no-border" markdown hidden>

- :custom-wind:{ .lg .middle }

    **Lean and expressive**
    We developed a lightweight ontology capable of reconstructing argumentative structures in text from minimal annotation of premises and conclusions, leveraging the inferential power of OWL reasoners.

- :custom-ruler-outline:{ .lg .middle .only-light }:custom-ruler:{ .lg .middle .only-dark }

    **Formally grounded**
    CONTRO implements the main features of ASPIC^+^, one of the most widely adopted formalisms for argumentation.

- :custom-brick-outline:{ .lg .middle .only-light }:custom-brick:{ .lg .middle .only-dark }

    **Built on design patterns**
    We chose to build upon the perspectivization ontology design pattern, extending it both extensionally and intensionally to support dialectical contexts.

- :fontawesome-solid-gears:{ .lg .middle }

    **Interoperable by design**
    By adopting DOLCE’s Descriptions and Situations model, the ontology is domain agnostic and supports principled ontological assertions: it can be applied independently of the framework chosen to describe the domain.

</div>

</section>
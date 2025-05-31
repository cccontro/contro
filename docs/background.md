---
description:
subtitle: Argumentation theory
icon: octicons/book-16
---

> In large measure dialectic is to our *factual* knowledge what logic is to our *formal* knowledge: a mechanism of rational validation. ==Nicholas Rescher, *Dialectics. A Controversy-Oriented Approach to the Theory of Knowledge*, p. xiii==

Argumentation theory studies how conclusions can be justified through structured reasoning, particularly in the presence of conflicting views. To achieve this, it must account for:

1. How arguments can be constructed; 
2. How arguments can be defeated;
3. How arguments can be defended against defeating counterarguments.

Early work produced many different systems with as many ways of representing knowledge, and this diversity reflects the limitations of formal logic in modeling real-life debate—defeasible, context-sensitive, and embedded in dialogue. This section surveys key responses to that challenge, tracing how different models have reconceived rational justification beyond the bounds of deductive form.

## Models

### Contextual approaches
The modern study of argumentation has been marked by a contention over the capacity of formal logic to represent real-world reasoning. The most skeptical in this regard was Stephen Toulmin, who in 1958 introduced a model of argument consisting of three core elements: the **claim**, the **grounds** (evidence supporting the claim), and the **warrant** (the principle explaining why the grounds support the claim). The model also included optional components such as **backing** (support for the warrant), **rebuttal** (conditions under which the claim might not hold), and **qualifier** (indicating the strength of the claim).

This is exemplified in Toulmin’s well-known case:

> **Claim**: Harry is a British subject.

> **Grounds**: Harry was born in Bermuda.

> **Warrant**: A man born in Bermuda will generally be a British subject.

> **Backing**: Statute and case law covering nationality.

> **Qualifier**: Presumably.

> **Rebuttal**: Unless his parents were foreign diplomats, or he has renounced his nationality.

Toulmin’s emphasis on warrants and backing drew directly from the structure of legal reasoning, where the strength of an argument rests not on its formal validity but on its grounding in the accepted procedures and norms of justification within a particular field. In this way, his model emphasized that reasoning varies across disciplines, depends on context, and must be judged by practical standards, laying the groundwork for a pragmatic and normative theory of argumentation.

Building on this approach, Douglas Walton extended the analysis of context-sensitive reasoning through a systematic catalog of **argumentation schemes**—structured templates for common types of arguments. Each scheme includes typical premises and conclusions, along with **critical questions** designed to test the argument’s strength and uncover hidden assumptions. For example, the *appeal to expert opinion* scheme can be represented as:

> E is an expert in domain D.

> E asserts that proposition P is true.

> P is within D.

> Therefore, P is true.

To evaluate this argument, one may ask: *How credible is E a source? Is E truly an expert in domain D? What exactly did E assert that implies P? Is E personally reliable? Is P consistent with what other experts assert? Is E’s assertion of P based on evidence?*

Walton regarded argument schemes as **dialogical devices**: each argument is a move in a dialogue, and the scheme it instantiates defines the set of appropriate responses (counterarguments) to that move. Schemes such as the appeal to expert opinion model source-based reasoning, and thereby offer a casuistic refinement of Toulmin’s notion of backing for warrants.

``` mermaid
---
config:
  fontFamily: var(--md-text-font-family)
  themeCSS: ".main text { fill: var(--md-default-fg-color) } .title text { font-weight: 700; } .labels text { font-weight: 300; } .border line { stroke: var(--md-default-fg-color--lighter); }"
  quadrantChart:
    chartWidth: 450
    chartHeight: 450
    pointTextPadding: 0
    pointRadius: 0
    titleFontSize: 16
    pointLabelFontSize: 16
  themeVariables:
    quadrantInternalBorderStrokeFill: var(--md-default-fg-color--lighter)
    quadrantExternalBorderStrokeFill: none
    quadrant1Fill: none
    quadrant2Fill: none
    quadrant3Fill: none
    quadrant4Fill: none
---
quadrantChart
    title Argumentation Theories by Formality and Normativity
    x-axis Descriptive --> Prescriptive
    y-axis Pragmatic --> Abstract
    Phan Minh Dung: [0.35, 0.95]
    John Pollock: [0.15, 0.75]
    Douglas Walton: [0.45, 0.4]
    Frans van Eemeren: [0.82, 0.25]
    Stephen Toulmin: [0.6, 0.1]
```

### Pollock's attacks
In the mid-1980s, John Pollock played a central role in applying **defeasible reasoning** to argumentation, addressing the limitations that made classical deductive logic unsuitable for representing real-world reasoning. In practice, argumentation follows the principles of **non-monotonic logic**, where the addition of new information, describing a more particular case, can invalidate previously valid conclusions.

One of Pollock’s key examples illustrates this:

> The object looks red.

> Therefore, the object is red.

> But the object is illuminated by a red light.

> So, it is not the case that the object would look red only if it were red.

In this case, the object appears red and is therefore presumed to be red until it is discovered that it is illuminated by a red light. The object may still be red, but it can no longer be concluded solely from its appearance. This kind of situation cannot be represented within classical deductive logic, where valid inferences are **monotonic**: if a conclusion follows from a premise, it continues to follow regardless of the addition of new premises. If A implies B, and A is true, then B must be true—no further information (C) can defeat B. But in everyday reasoning, conclusions are often **provisional**: they hold until new, relevant information defeats them. This is the core insight motivating non-monotonic logics and their application to argumentation.

Pollock formalized defeasible reasoning by distinguishing two kinds of attacks on arguments:

- **Undercut**, such as the red-light case, which challenges the connection between premise and conclusion without offering an alternative conclusion (under those conditions, one cannot know what color the object really is).

- **Rebuttal**, or distinction, which accepts the validity of the inference A → B but introduces a new premise C that leads to conclude that the case under consideration is a special case, an exception, and therefore to reach the opposite conclusion: A ∧ C → ¬B.

A canonical example of the latter is the Tweety case, first introduced by Raymond Reiter in 1980:

> Tweety is a bird.

> Birds typically fly.

> Therefore, Tweety flies.

> But Tweety is a penguin.

> Penguins don’t fly.

> So Tweety doesn’t fly.

Here, the initial generalization is rebutted by a specific exception. Notice also that in this case the premise *Tweety is a bird* is not only conceded but implicitly reaffirmed by the added information that Tweety is a penguin. This shows how deductive and defeasible reasoning can coexist within a single discourse: while the inference *Tweety is a penguin* → *Tweety is a bird* is deductively valid, the defeasible rule *Birds fly* is overridden by a more specific case.

Pollock’s system did not allow attacks on premises, but later formalisations recognized the need for a third type of attack to account for plausible reasoning. This attack, now known as **undermining**, negates an argument’s non-axiomatic premise and removes the support for its conclusion. Unlike undercuts, it does not invalidate the inference itself, but the conclusion remains unsupported unless the premise is defended. Undermining is currently being investigated in the context of belief revision, as it reduces the informational base from which agents draw further inferences.

<div class="mermaid">
<figcaption>Three Types of Attack</figcaption>
<div class="diagram">
<div>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-2.5 0 140 96">
  <g class="line">
    <path d="M 22.5 15.5 L 22.5 73.38"/>
    <path d="M 22.5 79.5 L 17.75 70 L 22.5 72.38 L 27.25 70 Z"/>
    <path d="M 87.5 48 L 22.5 48"/>
  </g>
  <g class="dot">
    <ellipse cx="22.5" cy="8" rx="7.5" ry="7.5"/>
    <ellipse cx="22.5" cy="88" rx="7.5" ry="7.5"/>
    <ellipse cx="95" cy="48" rx="7.5" ry="7.5"/>
  </g>
  <g class="cross">
    <path d="M 16.75 42.25 L 28.25 53.75 M 16.75 53.75 L 28.25 42.25"/>
  </g>
  <text x="-2.5" y="12.5">A</text>
  <text x="-2.5" y="92.5">B</text>
  <text x="110" y="52.5">C</text>
</svg>
<figcaption>Undercut<br/>C → ¬(A → B)</figcaption>
</div>

<div>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-2.5 0 140 96">
  <g class="line">
    <path d="M 22.5 15.5 L 22.5 73.38"/>
    <path d="M 102.5 15.5 L 102.5 73.38"/>
    <path d="M 22.5 79.5 L 17.75 70 L 22.5 72.38 L 27.25 70 Z"/>
    <path d="M 102.5 79.5 L 97.75 70 L 102.5 72.38 L 107.25 70 Z"/>
    <path d="M 95 88 L 30 88"/>
  </g>
  <g class="cross">
    <path d="M 30.75 82.25 L 42.25 93.75 M 30.75 93.75 L 42.25 82.25"/>
  </g>
  <g class="dot">
    <ellipse cx="22.5" cy="8" rx="7.5" ry="7.5"/>
    <ellipse cx="22.5" cy="88" rx="7.5" ry="7.5"/>
    <ellipse cx="102.5" cy="8" rx="7.5" ry="7.5"/>
    <ellipse cx="102.5" cy="88" rx="7.5" ry="7.5"/>
  </g>
  <text x="-2.5" y="12.5">A</text>
  <text x="-2.5" y="92.5">B</text>
  <text x="117.5" y="12.5">C</text>
  <text x="117.5" y="92.5">¬B</text>
</svg>
<figcaption>Rebuttal<br/>A ∧ C → ¬B</figcaption>
</div>

<div>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 140 175.5">
  <g class="line">
    <path d="m25,95v57.9"/>
    <path d="m97.5,87.5H32.5"/>
    <path d="m105,15v57.9"/>
    <path d="m25,159l-4.8-9.5,4.8,2.4,4.8-2.4-4.8,9.5Z"/>
    <path d="m105,79l-4.8-9.5,4.8,2.4,4.8-2.4-4.8,9.5Z"/>
  </g>
  <g class="cross">
    <path d="m33.2,81.8l11.5,11.5m-11.5,0l11.5-11.5"/>
  </g>
  <g class="dot">
    <circle cx="25" cy="87.5" r="7.5"/>
    <circle cx="25" cy="167.5" r="7.5"/>
    <circle cx="105" cy="7.5" r="7.5"/>
    <circle cx="105" cy="87.5" r="7.5"/>
  </g>
  <text transform="translate(0 92)">A</text>
  <text transform="translate(0 172)">B</text>
  <text transform="translate(120 92)">¬A</text>
  <text transform="translate(120.4 11.7)">C</text>
</svg>
<figcaption>Undermining<br/>C → ¬A</figcaption>
</div>
</div>
</div>

### Dung's abstract argumentation
In 1995, Phan Minh Dung introduced an abstract formalism for argumentation that separated the acceptability of arguments from both their internal structure and the specific nature of their conflicts. In his model, arguments are nodes in a directed graph connected by binary attack relations. A *calculus of opposition* is then applied to determine sets of acceptable arguments, called **extensions**, that represent rational stances if they are internally coherent (conflict-free) and externally defended. These extensions depend solely on attack and defense: a defense occurs when an argument in the set attacks an attacker of another member. The arguments of such an admissible extension are labelled as accepted, those attacked by an argument of the extension are defeated, and the others are undefined.

This set-theoretic approach decoupled abstract from structured argumentation, revolutionizing the field and enabling further mathematical development. Dung’s semantics now underpins most formal models of argumentation. It also helped clarify the distinction between *attack*—a non-evaluative conflict relation—and *defeat*, which is assigned after computing the extensions.

## ASPIC^+^

!!! info inline end "Rules beyond language"
	
	As usual in logic, inference rules lie outside the formal language from which they derive their variables. In ASPIC^+^, however, a **naming function** brings them into the object language, allowing them to be targeted by undercut attacks. These named rules are included in the knowledge base used to build arguments. To allow conflicts over a rule’s admissibility, opposing knowledge bases should not share the same inference rules.

The original ASPIC (Argumentation Service Platform with Integrated Components) was developed within a European project (2004–2007) to integrate, generalize, and extend existing approaches to structured argumentation. Its successor, ASPIC^+^ [@Modgil2013], first introduced in 2010, combines Dung’s abstract semantics with structured argumentation. It allows Pollock-style attacks to be formally represented while preserving a clear link to Dung’s acceptability criteria.

ASPIC^+^ is built around the following core components:

**Argumentation System**
: Consists of a logical language, a contradiction function (not necessarily symmetric) over formulas, and a set of inference rules—either *strict* (deductive) or *defeasible*.

**Knowledge Base**
: A subset of the language, divided into *axioms* (certain, not attackable) and *ordinary premises* (uncertain, attackable).

**Argument**
: A structure built from a set of premises, a conclusion, and a strict or defeasible inference rule connecting them. An argument is built on the basis of a knowledge base within a given argumentation system.

**Attack**
: A relation between two arguments where the conclusion of one contradicts an ordinary premise, the consequent of a defeasible rule, or a defeasible inference step in the other. These are called undermining, rebutting, and undercutting attacks, respectively.

ASPIC^+^ arguments generate abstract argumentation frameworks, to which Dung-like extension calculus can be applied to evaluate acceptability. Importantly, ASPIC^+^ is not a specific argumentation system, but a general framework for specifying such systems. It supports flexible instantiation, even with partial structures (e.g. only axioms or only ordinary premises), while ensuring that a complying system will satisfy some key rationality postualtes.

### Application in dialogical contexts

These structures define consequence relations from a fixed body of information, representing it statically. However, they are compatible with dynamic models of argumentative interaction, addressing critiques—such as Walton's—that arguments are meaningful only within dialogues or procedures. This tension is resolved by embedding argumentation logics within dialogue systems, where arguments become disputes between agents with distinct, evolving information states. Through interaction, agents may revise their beliefs and co-construct a joint theory of the issue, which also develops over time.
[@Prakken2011]
 
Si può vedere come abbiamo semplificato ASPIC^+^ in the [next section](model.md#adapting-aspic-structures). For a good overview see [@vanEemeren2014].
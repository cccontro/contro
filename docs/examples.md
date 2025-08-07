---
subtitle: CONTRO in action
icon: bootstrap/chat-quote-fill
extra_css:
  - assets/stylesheets/tei.css
toc_depth: 3
---

CONTRO’s aim is to extract opinions—both implicit and explicit—as they emerge within dialectical discourse through its structure. In this section, we demonstrate how illuminating this formal interpretation can be, using the first point of contention between Caro and Castelvetro as a case study.

We begin by reconstructing the arguments directly from the text. Then, we show how these arguments are formalized in the ontology, both as arguments and as perspectives. If you prefer to skip the textual excerpts, you can go directly to the [next section](#from-tree-to-graph).

## Argument analysis in text

Applying argumentation theory to textual analysis reveals latent argumentative structures that are often obscured by rhetorical strategies and implicatures. It enables us to:

- Reconstruct implicit premises and conclusions;
- Identify the opponent’s assertions that are the target of critique;
- Classify the type of attack (on premises, inference rules, or conclusions);
- Break down complex arguments into atomic ones, each with at most one conclusion.

For instance, an argument that **negates a premise** and **proposes an alternative conclusion** is, in fact, composed of two sub-arguments. The first is an undermining on the opponent’s argument that relies on the (positive form of the) negated premise.  The second sub-argument introduces a rebuttal (or distinction) that supports a contradictory conclusion. To do so, it should introduce an additional, often implicit, premise that justifies the new conclusion in light of the premises that remain acceptable. This structure exemplifies **non-monotonic reasoning**: attacking the premises alone is not enough to reach a different conclusion—it merely invalidates the opponent’s. To move from *pars destruens* to *pars construens*, further ontological commitments are required to support an alternative vision of the issue at stake.

This pattern is at play in [Caro’s response](#predellas-resentment) (under the pseudonym Predella) to the first point of Castelvetro’s critique. Our formalization of this reply also illustrates how Walton’s [scheme from expert opinion](background.md#contextual-approaches) is abstracted within the ASPIC^+^ framework: critical questions targeting the credibility of the expert or the validity of their claims function as undercutters, while the appeal to alternative expert opinions gives rise to a rebuttal [@Prakken2011, pp. 14–15]. Caro employs both moves, consistent with his rhetorical strategy of overwhelming the opponent through a multiplicity of attacks.

/// tab | English
--8<-- "tei/Apologia-Ragione-TEI-en.md"
///

/// tab | Italian
--8<-- "tei/Apologia-Ragione-TEI-it.md"
///

## From tree to graph




??? question "TEI Markup"

    Peculiar interests, haven't you? Congratulations, you have found the secret [TEI Documentation](tei/ns/1.0.md).

    In the project’s repository you will find the annotated text in [`Apologia-Ragione-TEI.xml`](https://github.com/cccontro/contro/blob/main/tei/Apologia-Ragione-TEI.xml) and the [`tei_arg.odd`](https://github.com/cccontro/contro/blob/main/tei/tei_arg.odd) schema it is validated against.


```xml title="XML/TEI annotation of an argument"
<div resp="#predella">
    <p><!-- Text passage annotated with @ana --></p>
    <note type="paraphrase">
        <list xml:id="CR1" type="argument" about="#disputed-words">
            <item type="premise"><ptr target="#s1"/></item>
            <item xml:id="s6" type="premise">There is no direct knowledge of Petrarch’s intention.</item>
            <item xml:id="s7" type="premise">Castelvetro is not a reliable interpreter of Petrarch’s mind.</item>
            <item xml:id="r3" type="rule" prev="#s1 #s6 #s7" next="#s8">Although Petrarch did not use the words, it’s impossible to determine whether he would have used them without reliable or direct knowledge of his intentions, which is unavailable.</item>
            <item xml:id="s8" type="conclusion" exclude="#r1">It is not possible to know whether Petrarch would have used those words.</item>
        </list>
    </note>
</div>
```

```turtle title="Extracted axioms about the argument"
:CR1 rdf:type arg:Argument ;
     arg:Conclusion :s8 ;
     arg:InferenceRule :r3 ;
     arg:Premise :s1 ,
                 :s6 ,
                 :s7 ;
     arg:Topic :disputed-words ;
     arg:by :predella .

:r3 arg:Antecedent :s1 ,
                   :s6 ,
                   :s7 ;
    arg:Consequent :s8 ;
    rdfs:comment "Although Petrarch did not use the words, it’s impossible to determine whether he would have used them without reliable or direct knowledge of his intentions, which is unavailable."@en .

:s1 rdfs:comment "Petrarch never used certain words."@en .

:s6 rdfs:comment "There is no direct knowledge of Petrarch’s intention."@en .

:s7 rdfs:comment "Castelvetro is not a reliable interpreter of Petrarch’s mind."@en .

:s8 arg:contradicts :r1 ;
    rdfs:comment "It is not possible to know whether Petrarch would have used those words."@en .
```

```turtle title="Inferred axioms about the argument"
:CR1 rdf:type dul:Situation ,
              arg:Argument ,
              arg:Conflict ,
              arg:Undercut , # (1)!
              persp:Perspectivisation ;
     dul:isSettingFor :AT_caro ,
                      :KB_caro ,
                      :disputed-words ,
                      :predella ,
                      :r3 ,
                      :s1 ,
                      :s6 ,
                      :s7 ,
                      :s8 ;
     dul:satisfies arg:Argument ,
                   persp:Perspectivisation ;
     arg:ArgumentationTheory :AT_caro ; # (2)!
     arg:Conclusion :s8 ;
     arg:InferenceRule :r3 ;
     arg:Premise :s1 ,
                 :s6 ,
                 :s7 ;
     arg:Topic :disputed-words ;
     arg:attacks :CV1 ;
     arg:by :predella ;
     persp:Background :KB_caro ;
     persp:Conceptualiser :predella ;
     persp:Cut :s8 ;
     persp:Eventuality :disputed-words ;
     persp:Lens :s1 ,
                :s6 ,
                :s7 .

:r3 rdf:type dul:Situation ,
             arg:InferenceRule ;
    dul:isSettingFor :s1 ,
                     :s6 ,
                     :s7 ,
                     :s8 ;
    dul:satisfies arg:InferenceRule ;
    arg:Antecedent :s1 ,
                   :s6 ,
                   :s7 ;
    arg:Consequent :s8 ;
    arg:extractedFrom :KB_caro ;
    rdfs:comment "Although Petrarch did not use the words, it’s impossible to determine whether he would have used them without reliable or direct knowledge of his intentions, which is unavailable."@en .

:s1 rdf:type dul:Situation ,
             arg:Antecedent ,
             arg:Premise ,
             persp:Lens ;
    dul:satisfies arg:Antecedent ,
                  arg:Premise ,
                  persp:Lens ;
    arg:extractedFrom :KB_caro ,
                      :KB_castelvetro ; # (3)!
    rdfs:comment "Petrarch never used certain words."@en .

:s6 rdf:type dul:Situation ,
             arg:Antecedent ,
             arg:Premise ,
             persp:Lens ;
    dul:satisfies arg:Antecedent ,
                  arg:Premise ,
                  persp:Lens ;
    arg:extractedFrom :KB_caro ;
    rdfs:comment "There is no direct knowledge of Petrarch’s intention."@en .

:s7 rdf:type dul:Situation ,
             arg:Antecedent ,
             arg:Premise ,
             persp:Lens ;
    dul:satisfies arg:Antecedent ,
                  arg:Premise ,
                  persp:Lens ;
    arg:extractedFrom :KB_caro ;
    rdfs:comment "Castelvetro is not a reliable interpreter of Petrarch’s mind."@en .

:s8 rdf:type dul:Situation ,
             arg:Conclusion ,
             arg:Consequent ,
             persp:Cut ;
    dul:satisfies arg:Conclusion ,
                  arg:Consequent ,
                  persp:Cut ;
    arg:contradicts :r1 ;
    arg:extractedFrom :KB_caro ;
    persp:shotThrough :s1 ,
                      :s6 ,
                      :s7 ;
    rdfs:comment "It is not possible to know whether Petrarch would have used those words."@en .
```

1. The argument attacks the inference rule of another argument.
2. An argumentation theory and the related knowledge base are shared among the aliases of an author.
3. This is a premise both opponents agree on.

## Draw your conclusion

Extracting arguments from this controversy showed the virtues and limitations of the ASPIC^+^ framework. For instance, since it doesn't allow to represent directly hypotetical statements and *reductio ad absurdum* arguments such as [Caro's point](#s19) about the subjection of poetic freedom to scriptural criteria, such argumentative structures had to be flattened into unified premises. On the other hand, it made it possible to distinctly portray the backfiring of an *ipse dixit* against the very author who had appealed to it, to reconstruct the supported standpoints behind the irony, and to represent the anticipation of the opponent's objections, effectively bringing out that although the two contentors both claim to be Petrarchists, they could not have more fundamentally different conceptions of what this consists of, citing the same authors to demonstrate the other's misunderstanding.

Since you have arrived here, you have probably made up your mind about the Caro–Castelvetro controversy. Now is the time to take sides.

<div class="strawpoll-embed" id="strawpoll_3RnYXmzwzye" style="height: 480px; max-width: 640px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;"><iframe id="strawpoll_iframe_3RnYXmzwzye" src="https://strawpoll.com/embed/3RnYXmzwzye" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe></div>

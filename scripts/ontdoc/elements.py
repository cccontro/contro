from ontdoc.utils import split_camel_case, get_relative_uri

from collections.abc import Iterable
from rdflib import URIRef, Namespace, RDF, RDFS, OWL
from rdflib.namespace import split_uri

from typing import Union, List


SWRL = Namespace("http://www.w3.org/2003/11/swrl#")

# Define OWL Type classes
labels = {
    OWL.Class: 'Class',
    OWL.ObjectProperty: 'Object Property',
    OWL.DatatypeProperty: 'Data Property',
    OWL.AnnotationProperty: 'Annotation Property',
    OWL.NamedIndividual: 'Individual',
    SWRL.Imp: 'Rule'
}

class OntoElement:
    _base = {}
    _extra = {}

    def __init__(el, uri: URIRef, owl_type: URIRef, suffix: str, context):
        # IMPORTANT! Cache the pointer to the element to avoid loop references
        context.entities[(uri, owl_type)] = el
        el.label = context.meta(RDFS.label, uri) or split_camel_case(split_uri(uri)[1])
        el.desc = context.meta(RDFS.comment, uri)
        el.href = get_relative_uri(context.uri, uri, suffix)
        el.uri = str(uri)
        el.owl_type = labels.get(owl_type)
        el.suffix = suffix
        el.also_defined_as = [
            context.format_node(uri, o) for o in context.g.objects(uri, RDF.type) if o != owl_type and o in labels
        ]
        el.see_also = context.meta(RDFS.seeAlso, uri, 'object', owl_type)

    def __repr__(el) -> str:
        return f"{el.__class__.__name__}({el.label})"
    
    def __getitem__(el, key):
        return getattr(el, key)
    
    def __eq__(el, other) -> bool:
        return el.__class__ == other.__class__ and el.label == other.label
    
    def __lt__(el, other) -> bool:
        if isinstance(other, OntoElement):
            return el.label.lower() < other.label.lower()
        elif isinstance(other, BNodeElement):
            return el.label.lower() < other.members[0].label.lower()
        elif isinstance(other, str):
            return el.label.lower() < other.lower()
        return False
    
    @property
    def has_extras(el):
        return any(getattr(el, attr) for attr in el._extra)
    
    @property
    def is_detail(el):
        return el.has_extras or bool(el.also_defined_as)
    
    def html(el) -> str:
        return f'<a class="{el.owl_type.lower().replace(' ', '_')}" href="{el.href}" title="{el.uri}">{el.label}</a><span class="sup" data-text="{el.suffix}" title="{el.owl_type}"></span>'


class Class(OntoElement):
    _base = {'equivalent': 'Equivalent to', 'subclass_of': 'Subclass of'}
    _extra = {
        'superclass_of': 'Superclass of',
        'in_range': 'In range of',
        'in_domain': 'In domain of',
        'disjoint': 'Disjoint with',
        'disjoint_union': 'Disjoint union',
        'keys': 'Key properties',
        'instances': 'Instances',
        'see_also': 'See also'
    }

    def __init__(el, uri: URIRef, context):
        super().__init__(uri, OWL.Class, 'c', context)
        el.equivalent = context.meta(OWL.equivalentClass, uri, 'both', OWL.Class)
        el.subclass_of = context.meta(RDFS.subClassOf, uri, 'object', OWL.Class)
        el.superclass_of = context.meta(RDFS.subClassOf, uri, 'subject', OWL.Class)
        el.in_range = context.meta(RDFS.range, uri, 'subject', OWL.ObjectProperty)
        el.in_domain = context.meta(RDFS.domain, uri, 'subject', OWL.ObjectProperty)
        el.disjoint = context.meta(OWL.disjointWith, uri, 'both', OWL.Class)
        el.disjoint_union = context.meta(OWL.disjointUnionOf, uri, 'object', OWL.Class)
        el.keys = context.meta(OWL.hasKey, uri, 'object', None)
        el.instances = context.meta(RDF.type, uri, 'subject', OWL.NamedIndividual)


class Property(OntoElement):
    _base = {'domain': 'Domain', 'range': 'Range'}
    _extra = {
        'equivalent': 'Equivalent to',
        'subproperty_of': 'Subproperty of',
        'superproperty_of': 'Superproperty of',
        'see_also': 'See also'
    }

    def __init__(el, uri: URIRef, owl_type: URIRef, suffix: str, context):
        super().__init__(uri, owl_type, suffix, context)
        el.equivalent = context.meta(OWL.equivalentProperty, uri, 'object', owl_type)
        el.subproperty_of = context.meta(RDFS.subPropertyOf, uri, 'object', owl_type)
        el.superproperty_of = context.meta(RDFS.subPropertyOf, uri, 'subject', owl_type)
        el.domain = context.meta(RDFS.domain, uri, 'object', OWL.Class)
        el.range = context.meta(RDFS.range, uri, 'object', OWL.Class)


class ObjectProperty(Property):
    _extra = {
        'equivalent': 'Equivalent to',
        'inverse': 'Inverse of',
        'subproperty_of': 'Subproperty of',
        'superproperty_of': 'Superproperty of',
        'chain': 'Superproperty of chain',
        'see_also': 'See also'
    }

    def __init__(el, uri: URIRef, context):
        super().__init__(uri, OWL.ObjectProperty, 'op', context)
        el.inverse = context.meta(OWL.inverseOf, uri, 'both', OWL.ObjectProperty)
        el.chain = context.meta(OWL.propertyChainAxiom, uri, 'object', OWL.ObjectProperty)


class DataProperty(Property):
    def __init__(el, uri: URIRef, context):
        super().__init__(uri, OWL.DatatypeProperty, 'dp', context)


class AnnotationProperty(Property):
    def __init__(el, uri: URIRef, context):
        super().__init__(uri, OWL.AnnotationProperty, 'ap', context)


class Individual(OntoElement):
    _base = {'of_class': 'Class'}
    _extra = {'assertions': 'Assertions', 'see_also': 'See also'}

    def __init__(el, uri: URIRef, context):
        super().__init__(uri, OWL.NamedIndividual, 'i', context)
        el.of_class = context.meta(RDF.type, uri, 'type', OWL.Class)
        el.assertions = context.meta(None, uri, 'predicate_objects', None)


class Rule(OntoElement):
    def __init__(el, uri: URIRef, context):
        super().__init__(uri, SWRL.Imp, 'r', context)
        el.antecedents = context.meta(SWRL.body, uri, 'object', OWL.ObjectProperty)
        el.consequent = context.meta(SWRL.head, uri, 'object', OWL.ObjectProperty)
        el.href = '#' + el.label.replace(' ', '_') if el.label else ''
        el.uri = ''

    @property
    def rule(el) -> str:
        return el.antecedents[0].html() + ' → ' + el.consequent[0].html()

# Blank Node classes
class BNodeElement:
    def __init__(el, *members: Union['OntoElement', 'BNodeElement']):
        if members and isinstance(members[0], Iterable):
            el.members = [e for m in members for e in m]
        else:
            el.members = members

    def __repr__(el) -> str:
        return f"{el.__class__.__name__}({', '.join([str(m) for m in el.members])})"
    
    def __eq__(el, other) -> bool:
        return el.__class__ == other.__class__ and all(m == o for m, o in zip(el.members, other.members))
    
    def __lt__(el, other) -> bool:
        if isinstance(other, BNodeElement):
            for m, o in zip(el.members, other.members):
                if m is not None and o is not None and m != o:
                    return m < o
        elif isinstance(other, OntoElement):
            for m in el.members:
                if m != other and not isinstance(m, str):
                    return m < other
        return False

    def html(el) -> str:
        return ' '.join(m.html() if isinstance(m, (OntoElement, BNodeElement)) else str(m) for m in el.members)
    
    def parens(el, m: Union['OntoElement', 'BNodeElement']) -> str:
        return f'({m.html()})' if isinstance(m, el.__class__) else m.html()


class Restriction(BNodeElement):
    def __init__(el, *members):
        super().__init__(*members)
        el.pred = members[0]
        el.quantifier = members[1]
        el.target = members[2]

    def html(el) -> str:
        return f'{el.pred.html()} {el.quantifier} {el.parens(el.target)}'
    
class Intersection(BNodeElement):
    def html(el) -> str:
        return ' and <br/>'.join(el.parens(m) for m in el.members)
    
class Disjunction(BNodeElement):
    def html(el) -> str:
        return ' or '.join(el.parens(m) for m in el.members)

class RDFList(BNodeElement):
    def html(el) -> str:
        return '</li><li>'.join(m.html() for m in el.members)
    
class Chain(BNodeElement):
    def html(el) -> str:
        return ' o '.join(m.html() for m in el.members)
    
class AtomList(BNodeElement):
    def html(el) -> str:
        return ' ∧ '.join(m.html() for m in el.members)
    
class Complement(BNodeElement):
    def __init__(el, target: Union['OntoElement', 'Restriction']):
        el.members = [target]
        el.target = target

    def __repr__(el) -> str:
        return f'Complement({el.target})'

    def html(el) -> str:
        return f'not({el.target.html()})'
    
class Inverse(BNodeElement):
    def __init__(el, target: 'ObjectProperty'):
        el.members = [target]
        el.target = target

    def __repr__(el) -> str:
        return f'Inverse({el.target})'

    def html(el) -> str:
        return f'inverse({el.target.html()})'
    
class Atom(BNodeElement):
    def __init__(el, pred: 'OntoElement', args: List[str]):
        el.members = [pred] + args
        el.pred = pred
        el.args = args

    def __repr__(el) -> str:
        return f'Atom({el.pred}, {", ".join(el.args)})'

    def html(el) -> str:
        arg_str = ', '.join('?' + arg for arg in el.args)
        return f'{el.pred.html()}({arg_str})'
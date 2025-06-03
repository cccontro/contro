from ontdoc.elements import (
    OntoElement,
    Class,
    ObjectProperty,
    DataProperty,
    AnnotationProperty,
    Individual,
    Rule,
    BNodeElement,
    Restriction,
    Intersection,
    Disjunction,
    Chain,
    Atom,
    AtomList,
    Complement,
    Inverse,
    SWRL
)
from ontdoc.utils import is_schema_predicate

from typing import Union, Dict, List, Tuple
from rdflib import Graph, URIRef, Literal, BNode, RDF, RDFS, OWL, DC, DCTERMS, VANN
from rdflib.namespace import split_uri


# Interface
class OntDoc:
    def __init__(self, path: str, lang: str = 'en'):
        # Set the language for literals
        self.lang = lang

        # Intialize the RDF graph
        self.g = Graph()
        self.g.parse(path, format='turtle')

        self.uri = next(self.g.subjects(RDF.type, OWL.Ontology), None)
        if self.uri is None:
            raise ValueError('No ontology URI found.')
        
        # Collect the namespaces used in the ontology
        used_ns = set()
        for p, o in self.g.predicate_objects():
            for term in (p, o):
                if isinstance(term, URIRef):
                    try:
                        used_ns.add(split_uri(term)[0])
                    except ValueError:
                        continue
        
        self.namespaces = dict(sorted((prefix, str(ns)) for prefix, ns in self.g.namespaces() if str(ns) in used_ns))

        # Initialize entities cache
        self.entities: Dict[Tuple[URIRef], 'OntoElement'] = {}

        # Initialize element classes
        self.owl_types = {
            OWL.Class: Class,
            OWL.ObjectProperty: ObjectProperty,
            OWL.DatatypeProperty: DataProperty,
            OWL.AnnotationProperty: AnnotationProperty,
            OWL.NamedIndividual: Individual,
            SWRL.Imp: Rule
        }

        # Ontology metadata
        self.title = self.meta(DCTERMS.title) or self.meta(DC.title)
        self.description = self.meta(DCTERMS.description) or self.meta(DC.description)
        self.creator = self.meta(DCTERMS.creator) or self.meta(DC.creator)
        self.created = self.meta(DCTERMS.created)
        self.modified = self.meta(DCTERMS.modified)
        self.version = self.meta(OWL.versionInfo)
        self.license = self.meta(DCTERMS.license)
        self.prefix = self.meta(VANN.preferredNamespacePrefix)
        self.bib = self.meta(RDFS.seeAlso)
        self.source = self.meta(DCTERMS.source) or self.meta(DC.source)

        # Ontology elements
        self.classes = self.get_properties(OWL.Class)
        self.object_properties = self.get_properties(OWL.ObjectProperty)
        self.data_properties = self.get_properties(OWL.DatatypeProperty)
        self.annotation_properties = self.get_properties(OWL.AnnotationProperty)
        self.individuals = self.get_properties(OWL.NamedIndividual)
        self.rules = self.get_properties(SWRL.Imp)


    # Methods 
    def get_properties(self, owl_type: URIRef) -> List['OntoElement']:
        entities = []

        for s in self.g.subjects(RDF.type, owl_type):
            if self.uri not in s and owl_type != SWRL.Imp:
                continue

            entities.append(self.format_node(s, owl_type))

        return sorted(entities)


    def meta(
        self,
        pred: URIRef,
        entity: URIRef = None,
        target: str = 'object',
        owl_type: URIRef = OWL.NamedIndividual
    ) -> Union['OntoElement', 'BNodeElement', List[Union['OntoElement', 'BNodeElement']], str, None]:
        g = self.g
        if entity is None:
            entity = self.uri
        match target:
            case 'object':
                data = [self.format_node(o, owl_type) for o in g.objects(entity, pred)]
            case 'subject':
                data = [self.format_node(o, owl_type) for o in g.subjects(pred, entity)]
            case 'both':
                data = [self.format_node(o, owl_type) for o in g.objects(entity, pred)] + \
                       [self.format_node(o, owl_type) for o in g.subjects(pred, entity) if not isinstance(o, BNode)]
            case 'predicate_objects':
                data = []
                for (p, o) in g.predicate_objects(entity):
                    if not is_schema_predicate(p):
                        object = self.format_node(o, OWL.NamedIndividual)
                        if isinstance(object, OntoElement):
                            predicate = self.format_node(p, OWL.ObjectProperty)
                        else:
                            predicate = self.format_node(p, OWL.DatatypeProperty)
                        data.append(BNodeElement(predicate, object))
            case 'type': # Exclude OWL types
                data = [
                    self.format_node(o, OWL.Class) for o in g.objects(entity, pred) if o not in self.owl_types
                ]
            case _:
                raise ValueError(f'Unknown target type for {pred}: {target}.')
        
        if not data:
            return None

        valid_data = [d for d in data if d is not None]

        if len(valid_data) == 1 and isinstance(valid_data[0], str):
            return valid_data[0]

        return sorted(valid_data)


    def format_node(self, s: Union[URIRef, BNode, Literal], owl_type: URIRef = OWL.NamedIndividual) -> Union['OntoElement', 'BNodeElement', str, None]:
        if (s, owl_type) in self.entities:
            return self.entities[(s, owl_type)]

        elif isinstance(s, BNode):
            if owl_type != SWRL.Imp:
                return self.format_bnode(s)
            return Rule(s, context=self)
        
        elif isinstance(s, URIRef):
            # Treat URLs not in the ontology namespaces as literals
            if not any(ns in s for ns in self.namespaces.values()):
                return str(s)
            return self.owl_types[owl_type](s, context=self) # Call the appropriate class constructor
        
        elif isinstance(s, Literal):
            # Exclude other languages
            if s.language == self.lang or s.language is None:
                return str(s)
            
        else:
            return str(s)
        

    def parse_list(self, head):
        items = []
        while head and head != RDF.nil:
            items.append(self.g.value(head, RDF.first))
            head = self.g.value(head, RDF.rest)
        return items


    def format_bnode(self, s: BNode) -> 'BNodeElement':
        g = self.g
        if (s, RDF.type, OWL.Restriction) in g:
            pred = self.format_node(g.value(s, OWL.onProperty), OWL.ObjectProperty)

            if (s, OWL.someValuesFrom, None) in g:
                quantifier = 'some'
                target = self.format_node(g.value(s, OWL.someValuesFrom), OWL.Class)
            elif (s, OWL.allValuesFrom, None) in g:
                quantifier = 'only'
                target = self.format_node(g.value(s, OWL.allValuesFrom), OWL.Class)
            elif (s, OWL.hasValue, None) in g:
                quantifier = 'value'
                target = self.format_node(g.value(s, OWL.hasValue), OWL.NamedIndividual)
            elif (s, OWL.onClass, None) in g:
                target = self.format_node(g.value(s, OWL.onClass), OWL.Class)
                for (cardinality, p) in [('min', OWL.minQualifiedCardinality), ('max', OWL.maxQualifiedCardinality), ('exactly', OWL.qualifiedCardinality)]:
                    v = g.value(s, p)
                    if v is not None:
                        quantifier = f'{cardinality} {v}'
                        break

            return Restriction(pred, quantifier, target)

        elif (s, OWL.intersectionOf, None) in g:
            members = self.parse_list(g.value(s, OWL.intersectionOf))
            return Intersection(self.format_node(m, OWL.Class) for m in members)

        elif (s, OWL.unionOf, None) in g:
            members = self.parse_list(g.value(s, OWL.unionOf))
            return Disjunction(self.format_node(m, OWL.Class) for m in members)

        elif (s, OWL.complementOf, None) in g:
            return Complement(self.format_node(g.value(s, OWL.complementOf), OWL.Class))
        
        elif (s, OWL.inverseOf, None) in g:
            return Inverse(self.format_node(g.value(s, OWL.inverseOf), OWL.ObjectProperty))
             
        elif (s, RDF.type, SWRL.AtomList) in g:
            return AtomList(self.swrl_atom(a) for a in self.parse_list(s))
        
        elif (None, OWL.disjointUnionOf, s) in g:
            return Disjunction(self.format_node(m, OWL.Class) for m in self.parse_list(s))

        else: # Chain
            return Chain(self.format_node(m, OWL.ObjectProperty) for m in self.parse_list(s))

    
    def swrl_atom(self, atom):
        g = self.g
        match g.value(atom, RDF.type):
            case SWRL.ClassAtom:
                pred = self.format_node(g.value(atom, SWRL.classPredicate), OWL.Class)
                args = [g.value(atom, SWRL.argument1)]
            case SWRL.IndividualPropertyAtom:
                pred = self.format_node(g.value(atom, SWRL.propertyPredicate), OWL.ObjectProperty)
                args = [g.value(atom, SWRL[f'argument{i}']) for i in range(1, 3)]
            case SWRL.DatavaluedPropertyAtom:
                pred = self.format_node(g.value(atom, SWRL.propertyPredicate), OWL.DatatypeProperty)
                args = [g.value(atom, SWRL[f'argument{i}']) for i in range(1, 3)]
            case SWRL.BuiltInAtom:
                pred = self.format_node(g.value(atom, SWRL.builtin))
                args = self.parse_list(g.value(atom, SWRL.arguments))
            case _:
                return None

        return Atom(pred, [split_uri(a)[1] for a in args])
    

    @property
    def elements(self) -> List[Tuple[str, List['OntoElement']]]:
        return [
            ('Classes', self.classes),
            ('Object Properties', self.object_properties),
            ('Data Properties', self.data_properties),
            ('Annotation Properties', self.annotation_properties),
            ('Individuals', self.individuals),
            ('Rules', self.rules)
        ]
    
    @property
    def metadata(self) -> List[Tuple[str, List['OntoElement']]]:
        return [
            ('IRI', self.uri.n3()),
            ('Version', self.version),
            ('Release', self.created),
            ('Last update', self.modified),
            ('Authors', ', '.join(self.creator) if isinstance(self.creator, list) else self.creator),
            ('Source', '<'+self.source+'>' if self.source else self.source)
        ]
from rdflib import Graph, Literal, URIRef, BNode, RDF, RDFS, OWL, DC, DCTERMS, VANN
from rdflib.namespace import split_uri

class OWLType:
    _base_properties = {
        'comment': (RDFS.comment, 'objects', None)
    }

    def __init__(self, label, suffix, properties=None):
        self.label = label
        self.suffix = suffix
        self.properties = dict(self._base_properties)
        if properties:
            self.properties.update(properties)


class PropertyType(OWLType):
    _base_properties = dict(OWLType._base_properties)
    _base_properties.update({
        'domain': (RDFS.domain, 'objects', OWL.Class),
        'range': (RDFS.range, 'objects', OWL.Class),
        'superproperty': (RDFS.subPropertyOf, 'objects', None),
        'subproperty': (RDFS.subPropertyOf, 'subjects', None),
        'equivalent': (OWL.equivalentProperty, 'objects', None),
    })


class OntDoc:
    def __init__(self, path):
        self.g = Graph()
        self.g.parse(path, format='turtle')
        self.uri = next(self.g.subjects(RDF.type, OWL.Ontology), None)
        if self.uri is None:
            raise ValueError('No ontology URI found.')
        self.namespaces = {ns[1] for ns in self.g.namespaces()}

        self.owl_types = {
            OWL.Class: OWLType('Class', 'c', {
                'superclass': (RDFS.subClassOf, 'objects', OWL.Class),
                'subclass': (RDFS.subClassOf, 'subjects', OWL.Class),
                'equivalent': (OWL.equivalentClass, 'both', OWL.Class),
                'disjoint': (OWL.disjointWith, 'both', OWL.Class),
                'disjoint_union': (OWL.disjointUnionOf, 'objects', OWL.Class),
                'inrange': (RDFS.range, 'subjects', OWL.ObjectProperty),
                'indomain': (RDFS.domain, 'subjects', OWL.ObjectProperty),
                'instances': (RDF.type, 'subjects', OWL.NamedIndividual)
            }),
            OWL.ObjectProperty: PropertyType('Object Property', 'op', {
                'inverse': (OWL.inverseOf, 'both', OWL.ObjectProperty),
                'chain': (OWL.propertyChainAxiom, 'objects', None)
            }),
            OWL.DatatypeProperty: PropertyType('Datatype Property', 'dp'),
            OWL.AnnotationProperty: PropertyType('Annotation Property', 'ap'),
            OWL.NamedIndividual: OWLType('Individual', 'i', {
                'class': (RDF.type, 'class', OWL.Class),
                'assertions': (None, 'predicate_objects', OWL.NamedIndividual)
            })
        }

        self.metadata = {
            'title': self.meta(DCTERMS.title) or self.meta(DC.title),
            'description': self.meta(DCTERMS.description) or self.meta(DC.description),
            'creator': self.meta(DCTERMS.creator) or self.meta(DC.creator),
            'created': self.meta(DCTERMS.created),
            'modified': self.meta(DCTERMS.modified),
            'version': self.meta(OWL.versionInfo),
            'license': self.meta(DCTERMS.license),
            'prefix': self.meta(VANN.preferredNamespacePrefix)
        }

        self.classes = self.get_properties(OWL.Class)
        self.object_properties = self.get_properties(OWL.ObjectProperty)
        self.datatype_properties = self.get_properties(OWL.DatatypeProperty)
        self.annotation_properties = self.get_properties(OWL.AnnotationProperty)
        self.individuals = self.get_properties(OWL.NamedIndividual)


    # Methods
    def is_schema_predicate(self, p):
        return (p in RDF) or (p in OWL) or (p in RDFS)
    

    def meta(self, pred, entity = None, target = 'objects', owl_type = OWL.NamedIndividual):
        g = self.g
        if entity is None:
            entity = self.uri
        match target:
            case 'objects':
                data = [self.format_node(o, owl_type) for o in g.objects(entity, pred)]
            case 'subjects':
                data = [self.format_node(o, owl_type) for o in g.subjects(entity, pred)]
            case 'both':
                data = [self.format_node(o, owl_type) for o in g.objects(entity, pred)] + \
                    [self.format_node(o, owl_type) for o in g.subjects(entity, pred)]
            case 'predicate_objects':
                data = [[self.format_node(p, OWL.ObjectProperty), self.format_node(o, OWL.NamedIndividual)] for (p, o) in g.predicate_objects(entity) if not self.is_schema_predicate(p)]
            case 'class':
                data = [self.format_node(o, OWL.Class) for o in g.objects(entity, pred) if o not in self.owl_types]
            case _:
                raise ValueError(f'Unknown target type for {pred}: {target}.')
        
        if not data:
            return None
        return data[0] if len(data) == 1 else data


    def parse_list(self, head):
        items = []
        while head and head != RDF.nil:
            items.append(self.g.value(head, RDF.first))
            head = self.g.value(head, RDF.rest)
        return items


    def format_node(self, s, owl_type = OWL.NamedIndividual):
        if isinstance(s, BNode):
            return self.bnode(s)
        elif isinstance(s, URIRef):
            if not any(ns in s for ns in self.namespaces):
                return { 'type': 'literal', 'value': str(s) }

            return {
                'type': 'uri',
                'uri': str(s),
                'label': self.meta(RDFS.label, s) or split_uri(s)[1],
                'owl_type': self.owl_types[owl_type].label,
                'href': f'{split_uri(s)[1]}_{self.owl_types[owl_type].suffix}' if str(s).startswith(self.uri) else str(s)
            }
        elif isinstance(s, Literal):
            return {
                'type': 'literal',
                'value': str(s),
                'datatype': str(s.datatype) if s.datatype else None,
                'lang': s.language
            }
        else:
            return {
                'type': 'unknown',
                'value': str(s)
            }


    def bnode(self, s):
        g = self.g
        if (s, RDF.type, OWL.Restriction) in g:
            r = {}
            r['type'] = 'restriction'
            r['property'] = self.format_node(g.value(s, OWL.onProperty), OWL.ObjectProperty)

            if (s, OWL.someValuesFrom, None) in g:
                r['quantifier'] = 'some'
                r['target'] = self.format_node(g.value(s, OWL.someValuesFrom), OWL.Class)
            elif (s, OWL.allValuesFrom, None) in g:
                r['quantifier'] = 'only'
                r['target'] = self.format_node(g.value(s, OWL.allValuesFrom), OWL.Class)
            elif (s, OWL.hasValue, None) in g:
                r['quantifier'] = 'value'
                r['target'] = self.format_node(g.value(s, OWL.hasValue), OWL.NamedIndividual)
            elif (s, OWL.onClass, None) in g:
                r['target'] = self.format_node(g.value(s, OWL.onClass), OWL.Class)
                for (cardinality, p) in [('min', OWL.minQualifiedCardinality), ('max', OWL.maxQualifiedCardinality), ('exactly', OWL.qualifiedCardinality)]:
                    v = g.value(s, p)
                    if v:
                        r['quantifier'] = f'{cardinality} {v}'
                        break
            return r

        elif (s, OWL.intersectionOf, None) in g:
            operands = self.parse_list(g.value(s, OWL.intersectionOf))
            return {
                'type': 'intersection',
                'target': [self.format_node(o, OWL.Class) for o in operands]
            }

        elif (s, OWL.unionOf, None) in g:
            operands = self.parse_list(g.value(s, OWL.unionOf))
            return {
                'type': 'union',
                'target': [self.format_node(o, OWL.Class) for o in operands]
            }

        elif (s, OWL.complementOf, None) in g:
            return {
                'type': 'complement',
                'target': self.format_node(g.value(s, OWL.complementOf), OWL.Class)
            }
        
        elif (s, OWL.inverseOf, None) in g:
            return {
                'type': 'inverse',
                'target': self.format_node(g.value(s, OWL.inverseOf), OWL.ObjectProperty)
            }
        
        else: # Chain
            return {
                'type': 'chain',
                'target': [self.format_node(c, OWL.ObjectProperty) for c in self.parse_list(s)]
            }
        
    def get_properties(self, owl_type):
        entities = []
        properties = self.owl_types[owl_type].properties

        for s in self.g.subjects(RDF.type, owl_type):
            if not str(s).startswith(self.uri):
                continue

            ann = self.format_node(s, owl_type)

            for label, (p, target, target_owl_type) in properties.items():
                ann[label] = self.meta(p, s, target, target_owl_type or owl_type)

            ann['also_defined_as'] = [self.format_node(s, o) for o in self.g.objects(s, RDF.type) if o != owl_type and o in self.owl_types]
            entities.append(ann)

        return entities
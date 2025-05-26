import re
from rdflib import Graph, URIRef, Literal, BNode, Namespace, RDF, RDFS, OWL, DC, DCTERMS, VANN
from rdflib.namespace import split_uri

SWRL = Namespace("http://www.w3.org/2003/11/swrl#")

# Classes
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
        'subproperty': (RDFS.subPropertyOf, 'objects', None),
        'superproperty': (RDFS.subPropertyOf, 'subjects', None),
        'equivalent': (OWL.equivalentProperty, 'objects', None),
    })


# Interface
class OntDoc:
    def __init__(self, path, lang='en'):
        self.g = Graph()
        self.g.parse(path, format='turtle')
        self.uri = next(self.g.subjects(RDF.type, OWL.Ontology), None)
        if self.uri is None:
            raise ValueError('No ontology URI found.')
        
        used_ns = set()
        for p, o in self.g.predicate_objects():
            for term in (p, o):
                if isinstance(term, URIRef):
                    try:
                        used_ns.add(split_uri(term)[0])
                    except ValueError:
                        continue
        self.namespaces = dict(sorted((prefix, str(ns)) for prefix, ns in self.g.namespaces() if str(ns) in used_ns))

        self.owl_types = {
            OWL.Class: OWLType('Class', 'c', {
                'subclass_of': (RDFS.subClassOf, 'objects', OWL.Class),
                'superclass_of': (RDFS.subClassOf, 'subjects', OWL.Class),
                'equivalent': (OWL.equivalentClass, 'both', OWL.Class),
                'disjoint': (OWL.disjointWith, 'both', OWL.Class),
                'disjoint_union': (OWL.disjointUnionOf, 'objects', OWL.Class),
                'in_range': (RDFS.range, 'subjects', OWL.ObjectProperty),
                'in_domain': (RDFS.domain, 'subjects', OWL.ObjectProperty),
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
            }),
            SWRL.Imp: OWLType('Rule', 'r', {
                'antecedents': (SWRL.body, 'objects', OWL.ObjectProperty),
                'consequent': (SWRL.head, 'objects', OWL.ObjectProperty)
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
        self.rules = self.get_properties(SWRL.Imp)


    # Methods
    def get_properties(self, owl_type):
        entities = []
        properties = self.owl_types[owl_type].properties

        for s in self.g.subjects(RDF.type, owl_type):
            if not str(s).startswith(self.uri) and owl_type != SWRL.Imp:
                continue

            ann = self.format_node(s, owl_type)

            for label, (p, target, target_owl_type) in properties.items():
                ann[label] = self.meta(p, s, target, target_owl_type or owl_type)

            if not isinstance(s, BNode):
                ann['also_defined_as'] = [self.format_node(s, o) for o in self.g.objects(s, RDF.type) if o != owl_type and o in self.owl_types]
            entities.append(ann)

        return sorted(entities, key=lambda x: x.get('label', {}).get('value', 'zzz').lower())
    
    def split_camel_case(self, s):
        return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', s)
    

    def meta(self, pred, entity = None, target = 'objects', owl_type = OWL.NamedIndividual):
        g = self.g
        if entity is None:
            entity = self.uri
        match target:
            case 'objects':
                data = [self.format_node(o, owl_type) for o in g.objects(entity, pred)]
            case 'subjects':
                data = [self.format_node(o, owl_type) for o in g.subjects(pred, entity)]
            case 'both':
                data = [self.format_node(o, owl_type) for o in g.objects(entity, pred)] + \
                    [self.format_node(o, owl_type) for o in g.subjects(pred, entity)]
            case 'predicate_objects':
                data = [[self.format_node(p, OWL.ObjectProperty), self.format_node(o, OWL.NamedIndividual)] for (p, o) in g.predicate_objects(entity) if not self.is_schema_predicate(p)]
            case 'class':
                data = [self.format_node(o, OWL.Class) for o in g.objects(entity, pred) if o not in self.owl_types]
            case _:
                raise ValueError(f'Unknown target type for {pred}: {target}.')
        
        if not data:
            return None
        return data[0] if len(data) == 1 else data
    

    def is_schema_predicate(self, p):
        return (p in RDF) or (p in OWL) or (p in RDFS)


    def format_node(self, s, owl_type = OWL.NamedIndividual):
        if isinstance(s, BNode):
            if owl_type != SWRL.Imp:
                return self.bnode(s)
            return {
                'type': 'rule',
                'label': self.meta(RDFS.label, s),
                'sup': self.owl_types[owl_type].suffix,
            }
        elif isinstance(s, URIRef):
            if not any(ns in s for ns in self.namespaces.values()):
                return { 'type': 'literal', 'value': str(s), 'datatype': None, 'lang': None }

            return {
                'type': 'uri',
                'uri': str(s),
                'label': self.meta(RDFS.label, s) or self.format_node(self.split_camel_case(split_uri(s)[1])),
                'owl_type': self.owl_types[owl_type].label,
                'sup': self.owl_types[owl_type].suffix,
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
                'type': 'literal',
                'value': str(s),
                'datatype': None,
                'lang': None
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
             
        elif (s, RDF.type, SWRL.AtomList) in g:
            return [self.swrl_atom(a) for a in self.parse_list(s)]
        
        else: # Chain
            return [self.format_node(c, OWL.ObjectProperty) for c in self.parse_list(s)]
        

    def parse_list(self, head):
        items = []
        while head and head != RDF.nil:
            items.append(self.g.value(head, RDF.first))
            head = self.g.value(head, RDF.rest)
        return items
    

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
                return {'predicate': None, 'args': []}

        return {
            'predicate': pred,
            'args': [split_uri(a)[1] for a in args]
        }
    

doc = OntDoc('docs/ont/arg.ttl')

#from pprint import pprint
#pprint([(x.get('label', {}).get('value', 'zzz'), x.get('type')) for x in doc.classes])
#pprint(doc.classes[0])

'''
# Example class output:
{'also_defined_as': [{'href': 'Argument_i',
                      'label': {'datatype': None,
                                'lang': None,
                                'type': 'literal',
                                'value': 'Argument'},
                      'owl_type': 'Individual',
                      'sup': 'i',
                      'type': 'uri',
                      'uri': 'https://w3id.org/contro/arg#Argument'}],
 'comment': {'datatype': None,
             'lang': 'en',
             'type': 'literal',
             'value': 'An argument is defined relative to an argumentation '
                      'theory and a knowledge base. Its premises are the '
                      'formulas and inference rule from the knowledge base, '
                      'its conclusion is the formula inferred from the '
                      'premises through the application of said inference '
                      'rule.'},
 'disjoint': {'href': 'Statement_c',
              'label': {'datatype': None,
                        'lang': None,
                        'type': 'literal',
                        'value': 'Statement'},
              'owl_type': 'Class',
              'sup': 'c',
              'type': 'uri',
              'uri': 'https://w3id.org/contro/arg#Statement'},
 'disjoint_union': None,
 'equivalent': {'property': {'href': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies',
                             'label': {'datatype': None,
                                       'lang': None,
                                       'type': 'literal',
                                       'value': 'satisfies'},
                             'owl_type': 'Object Property',
                             'sup': 'op',
                             'type': 'uri',
                             'uri': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#satisfies'},
                'quantifier': 'value',
                'target': {'href': 'Argument_i',
                           'label': {'datatype': None,
                                     'lang': None,
                                     'type': 'literal',
                                     'value': 'Argument'},
                           'owl_type': 'Individual',
                           'sup': 'i',
                           'type': 'uri',
                           'uri': 'https://w3id.org/contro/arg#Argument'},
                'type': 'restriction'},
 'href': 'Argument_c',
 'indomain': None,
 'inrange': {'href': 'attacks_op',
             'label': {'datatype': None,
                       'lang': None,
                       'type': 'literal',
                       'value': 'attacks'},
             'owl_type': 'Object Property',
             'sup': 'op',
             'type': 'uri',
             'uri': 'https://w3id.org/contro/arg#attacks'},
 'instances': None,
 'label': {'datatype': None,
           'lang': None,
           'type': 'literal',
           'value': 'Argument'},
 'owl_type': 'Class',
 'subclass': [{'href': 'ArgumentationTheorySituation_c',
               'label': {'datatype': None,
                         'lang': None,
                         'type': 'literal',
                         'value': 'Argumentation Theory Situation'},
               'owl_type': 'Class',
               'sup': 'c',
               'type': 'uri',
               'uri': 'https://w3id.org/contro/arg#ArgumentationTheorySituation'},
              {'property': {'href': 'Author_op',
                            'label': {'datatype': None,
                                      'lang': None,
                                      'type': 'literal',
                                      'value': 'Author'},
                            'owl_type': 'Object Property',
                            'sup': 'op',
                            'type': 'uri',
                            'uri': 'https://w3id.org/contro/arg#Author'},
               'quantifier': 'some',
               'target': {'href': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent',
                          'label': {'datatype': None,
                                    'lang': None,
                                    'type': 'literal',
                                    'value': 'Agent'},
                          'owl_type': 'Class',
                          'sup': 'c',
                          'type': 'uri',
                          'uri': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent'},
               'type': 'restriction'},
              {'property': {'href': 'Premise_op',
                            'label': {'datatype': None,
                                      'lang': None,
                                      'type': 'literal',
                                      'value': 'Premise'},
                            'owl_type': 'Object Property',
                            'sup': 'op',
                            'type': 'uri',
                            'uri': 'https://w3id.org/contro/arg#Premise'},
               'quantifier': 'some',
               'target': {'href': 'InferenceRule_c',
                          'label': {'datatype': None,
                                    'lang': None,
                                    'type': 'literal',
                                    'value': 'Inference Rule'},
                          'owl_type': 'Class',
                          'sup': 'c',
                          'type': 'uri',
                          'uri': 'https://w3id.org/contro/arg#InferenceRule'},
               'type': 'restriction'},
              {'property': {'href': 'Premise_op',
                            'label': {'datatype': None,
                                      'lang': None,
                                      'type': 'literal',
                                      'value': 'Premise'},
                            'owl_type': 'Object Property',
                            'sup': 'op',
                            'type': 'uri',
                            'uri': 'https://w3id.org/contro/arg#Premise'},
               'quantifier': 'some',
               'target': {'href': 'Statement_c',
                          'label': {'datatype': None,
                                    'lang': None,
                                    'type': 'literal',
                                    'value': 'Statement'},
                          'owl_type': 'Class',
                          'sup': 'c',
                          'type': 'uri',
                          'uri': 'https://w3id.org/contro/arg#Statement'},
               'type': 'restriction'},
              {'property': {'href': 'Topic_op',
                            'label': {'datatype': None,
                                      'lang': None,
                                      'type': 'literal',
                                      'value': 'Topic'},
                            'owl_type': 'Object Property',
                            'sup': 'op',
                            'type': 'uri',
                            'uri': 'https://w3id.org/contro/arg#Topic'},
               'quantifier': 'some',
               'target': {'href': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation',
                          'label': {'datatype': None,
                                    'lang': None,
                                    'type': 'literal',
                                    'value': 'Situation'},
                          'owl_type': 'Class',
                          'sup': 'c',
                          'type': 'uri',
                          'uri': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation'},
               'type': 'restriction'},
              {'property': {'href': 'KnowledgeBase_op',
                            'label': {'datatype': None,
                                      'lang': None,
                                      'type': 'literal',
                                      'value': 'Knowledge Base'},
                            'owl_type': 'Object Property',
                            'sup': 'op',
                            'type': 'uri',
                            'uri': 'https://w3id.org/contro/arg#KnowledgeBase'},
               'target': {'href': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation',
                          'label': {'datatype': None,
                                    'lang': None,
                                    'type': 'literal',
                                    'value': 'Situation'},
                          'owl_type': 'Class',
                          'sup': 'c',
                          'type': 'uri',
                          'uri': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation'},
               'type': 'restriction'},
              {'property': {'href': 'Conclusion_op',
                            'label': {'datatype': None,
                                      'lang': None,
                                      'type': 'literal',
                                      'value': 'Conclusion'},
                            'owl_type': 'Object Property',
                            'sup': 'op',
                            'type': 'uri',
                            'uri': 'https://w3id.org/contro/arg#Conclusion'},
               'quantifier': 'max 1',
               'target': {'href': 'Statement_c',
                          'label': {'datatype': None,
                                    'lang': None,
                                    'type': 'literal',
                                    'value': 'Statement'},
                          'owl_type': 'Class',
                          'sup': 'c',
                          'type': 'uri',
                          'uri': 'https://w3id.org/contro/arg#Statement'},
               'type': 'restriction'}],
 'sup': 'c',
 'superclass': {'href': 'Conflict_c',
                'label': {'datatype': None,
                          'lang': None,
                          'type': 'literal',
                          'value': 'Conflict'},
                'owl_type': 'Class',
                'sup': 'c',
                'type': 'uri',
                'uri': 'https://w3id.org/contro/arg#Conflict'},
 'type': 'uri',
 'uri': 'https://w3id.org/contro/arg#Argument'}


# Example object property output:
{'also_defined_as': [],
 'chain': None,
 'comment': None,
 'domain': None,
 'equivalent': None,
 'href': 'attackedBy_op',
 'inverse': {'href': 'attacks_op',
             'label': {'datatype': None,
                       'lang': None,
                       'type': 'literal',
                       'value': 'attacks'},
             'owl_type': 'Object Property',
             'sup': 'op',
             'type': 'uri',
             'uri': 'https://w3id.org/contro/arg#attacks'},
 'label': {'datatype': None,
           'lang': None,
           'type': 'literal',
           'value': 'attacked By'},
 'owl_type': 'Object Property',
 'range': None,
 'subproperty': None,
 'sup': 'op',
 'superproperty': None,
 'type': 'uri',
 'uri': 'https://w3id.org/contro/arg#attackedBy'}
contro-py3.12francesca@cuspide:~/Documents/GitHub/contro$ /home/francesca/.cache/pypoetry/virtualenvs/contro-ePoNuWTb-py3.12/bin/python /home/francesca/Documents/GitHub/contro/scripts/ontdoc.py
{'also_defined_as': [],
 'chain': [[{'href': 'Conclusion_op',
             'label': {'datatype': None,
                       'lang': None,
                       'type': 'literal',
                       'value': 'Conclusion'},
             'owl_type': 'Object Property',
             'sup': 'op',
             'type': 'uri',
             'uri': 'https://w3id.org/contro/arg#Conclusion'},
            {'href': 'contradicts_op',
             'label': {'datatype': None,
                       'lang': None,
                       'type': 'literal',
                       'value': 'contradicts'},
             'owl_type': 'Object Property',
             'sup': 'op',
             'type': 'uri',
             'uri': 'https://w3id.org/contro/arg#contradicts'},
            {'target': {'href': 'Conclusion_op',
                        'label': {'datatype': None,
                                  'lang': None,
                                  'type': 'literal',
                                  'value': 'Conclusion'},
                        'owl_type': 'Object Property',
                        'sup': 'op',
                        'type': 'uri',
                        'uri': 'https://w3id.org/contro/arg#Conclusion'},
             'type': 'inverse'}],
           [{'href': 'Premise_op',
             'label': {'datatype': None,
                       'lang': None,
                       'type': 'literal',
                       'value': 'Premise'},
             'owl_type': 'Object Property',
             'sup': 'op',
             'type': 'uri',
             'uri': 'https://w3id.org/contro/arg#Premise'},
            {'href': 'contradicts_op',
             'label': {'datatype': None,
                       'lang': None,
                       'type': 'literal',
                       'value': 'contradicts'},
             'owl_type': 'Object Property',
             'sup': 'op',
             'type': 'uri',
             'uri': 'https://w3id.org/contro/arg#contradicts'},
            {'target': {'href': 'Premise_op',
                        'label': {'datatype': None,
                                  'lang': None,
                                  'type': 'literal',
                                  'value': 'Premise'},
                        'owl_type': 'Object Property',
                        'sup': 'op',
                        'type': 'uri',
                        'uri': 'https://w3id.org/contro/arg#Premise'},
             'type': 'inverse'}]],
 'comment': {'datatype': None,
             'lang': 'en',
             'type': 'literal',
             'value': 'The relationship between a Conflict and the argument it '
                      'targets.'},
 'domain': {'href': 'Conflict_c',
            'label': {'datatype': None,
                      'lang': None,
                      'type': 'literal',
                      'value': 'Conflict'},
            'owl_type': 'Class',
            'sup': 'c',
            'type': 'uri',
            'uri': 'https://w3id.org/contro/arg#Conflict'},
 'equivalent': None,
 'href': 'attacks_op',
 'inverse': None,
 'label': {'datatype': None,
           'lang': None,
           'type': 'literal',
           'value': 'attacks'},
 'owl_type': 'Object Property',
 'range': {'href': 'Argument_c',
           'label': {'datatype': None,
                     'lang': None,
                     'type': 'literal',
                     'value': 'Argument'},
           'owl_type': 'Class',
           'sup': 'c',
           'type': 'uri',
           'uri': 'https://w3id.org/contro/arg#Argument'},
 'subproperty': None,
 'sup': 'op',
 'superproperty': None,
 'type': 'uri',
 'uri': 'https://w3id.org/contro/arg#attacks'}


# Example individual output:
{'also_defined_as': [{'href': 'Argument_c',
                      'label': {'datatype': None,
                                'lang': None,
                                'type': 'literal',
                                'value': 'Argument'},
                      'owl_type': 'Class',
                      'sup': 'c',
                      'type': 'uri',
                      'uri': 'https://w3id.org/contro/arg#Argument'}],
 'assertions': [[{'href': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent',
                  'label': {'datatype': None,
                            'lang': None,
                            'type': 'literal',
                            'value': 'has Component'},
                  'owl_type': 'Object Property',
                  'sup': 'op',
                  'type': 'uri',
                  'uri': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent'},
                 {'href': 'Author_i',
                  'label': {'datatype': None,
                            'lang': None,
                            'type': 'literal',
                            'value': 'Author'},
                  'owl_type': 'Individual',
                  'sup': 'i',
                  'type': 'uri',
                  'uri': 'https://w3id.org/contro/arg#Author'}],
                [{'href': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent',
                  'label': {'datatype': None,
                            'lang': None,
                            'type': 'literal',
                            'value': 'has Component'},
                  'owl_type': 'Object Property',
                  'sup': 'op',
                  'type': 'uri',
                  'uri': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent'},
                 {'href': 'Conclusion_i',
                  'label': {'datatype': None,
                            'lang': None,
                            'type': 'literal',
                            'value': 'Conclusion'},
                  'owl_type': 'Individual',
                  'sup': 'i',
                  'type': 'uri',
                  'uri': 'https://w3id.org/contro/arg#Conclusion'}],
                [{'href': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent',
                  'label': {'datatype': None,
                            'lang': None,
                            'type': 'literal',
                            'value': 'has Component'},
                  'owl_type': 'Object Property',
                  'sup': 'op',
                  'type': 'uri',
                  'uri': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent'},
                 {'href': 'KnowledgeBase_i',
                  'label': {'datatype': None,
                            'lang': None,
                            'type': 'literal',
                            'value': 'Knowledge Base'},
                  'owl_type': 'Individual',
                  'sup': 'i',
                  'type': 'uri',
                  'uri': 'https://w3id.org/contro/arg#KnowledgeBase'}],
                [{'href': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent',
                  'label': {'datatype': None,
                            'lang': None,
                            'type': 'literal',
                            'value': 'has Component'},
                  'owl_type': 'Object Property',
                  'sup': 'op',
                  'type': 'uri',
                  'uri': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent'},
                 {'href': 'Premise_i',
                  'label': {'datatype': None,
                            'lang': None,
                            'type': 'literal',
                            'value': 'Premise'},
                  'owl_type': 'Individual',
                  'sup': 'i',
                  'type': 'uri',
                  'uri': 'https://w3id.org/contro/arg#Premise'}],
                [{'href': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent',
                  'label': {'datatype': None,
                            'lang': None,
                            'type': 'literal',
                            'value': 'has Component'},
                  'owl_type': 'Object Property',
                  'sup': 'op',
                  'type': 'uri',
                  'uri': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#hasComponent'},
                 {'href': 'Topic_i',
                  'label': {'datatype': None,
                            'lang': None,
                            'type': 'literal',
                            'value': 'Topic'},
                  'owl_type': 'Individual',
                  'sup': 'i',
                  'type': 'uri',
                  'uri': 'https://w3id.org/contro/arg#Topic'}]],
 'class': {'href': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description',
           'label': {'datatype': None,
                     'lang': None,
                     'type': 'literal',
                     'value': 'Description'},
           'owl_type': 'Class',
           'sup': 'c',
           'type': 'uri',
           'uri': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Description'},
 'comment': {'datatype': None,
             'lang': 'en',
             'type': 'literal',
             'value': 'An argument is defined relative to an argumentation '
                      'theory and a knowledge base. Its premises are the '
                      'formulas and inference rule from the knowledge base, '
                      'its conclusion is the formula inferred from the '
                      'premises through the application of said inference '
                      'rule.'},
 'href': 'Argument_i',
 'label': {'datatype': None,
           'lang': None,
           'type': 'literal',
           'value': 'Argument'},
 'owl_type': 'Individual',
 'sup': 'i',
 'type': 'uri',
 'uri': 'https://w3id.org/contro/arg#Argument'}


# Example rule output:
{'antecedents': [{'args': ['a', 'p'],
                  'predicate': {'href': 'Premise_op',
                                'label': {'datatype': None,
                                          'lang': None,
                                          'type': 'literal',
                                          'value': 'Premise'},
                                'owl_type': 'Object Property',
                                'sup': 'op',
                                'type': 'uri',
                                'uri': 'https://w3id.org/contro/arg#Premise'}},
                 {'args': ['a', 'c'],
                  'predicate': {'href': 'Conclusion_op',
                                'label': {'datatype': None,
                                          'lang': None,
                                          'type': 'literal',
                                          'value': 'Conclusion'},
                                'owl_type': 'Object Property',
                                'sup': 'op',
                                'type': 'uri',
                                'uri': 'https://w3id.org/contro/arg#Conclusion'}},
                 {'args': ['i', 'p'],
                  'predicate': {'href': 'Antecedent_op',
                                'label': {'datatype': None,
                                          'lang': None,
                                          'type': 'literal',
                                          'value': 'Antecedent'},
                                'owl_type': 'Object Property',
                                'sup': 'op',
                                'type': 'uri',
                                'uri': 'https://w3id.org/contro/arg#Antecedent'}},
                 {'args': ['i', 'c'],
                  'predicate': {'href': 'Consequent_op',
                                'label': {'datatype': None,
                                          'lang': None,
                                          'type': 'literal',
                                          'value': 'Consequent'},
                                'owl_type': 'Object Property',
                                'sup': 'op',
                                'type': 'uri',
                                'uri': 'https://w3id.org/contro/arg#Consequent'}}],
 'comment': {'datatype': None,
             'lang': None,
             'type': 'literal',
             'value': 'An argumentation that concludes B from A has the '
                      'implicit premise that there exists an implication from '
                      'A to B'},
 'consequent': [{'args': ['a', 'i'],
                 'predicate': {'href': 'Premise_op',
                               'label': {'datatype': None,
                                         'lang': None,
                                         'type': 'literal',
                                         'value': 'Premise'},
                               'owl_type': 'Object Property',
                               'sup': 'op',
                               'type': 'uri',
                               'uri': 'https://w3id.org/contro/arg#Premise'}}],
 'label': {'datatype': None, 'lang': None, 'type': 'literal', 'value': 'S1'},
 'sup': 'r',
 'type': 'rule'}

'''
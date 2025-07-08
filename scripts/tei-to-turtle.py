import argparse

import xml.etree.ElementTree as ET
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS, PROV, OWL

import write_if_changed

BASE = 'https://w3id.org/contro/data'

# RDF namespaces
ARG = Namespace('https://w3id.org/contro/arg#')
DATA = Namespace(BASE + '#')
DUL = Namespace('http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#')

# XML namespaces
NS = {'xml': 'http://www.w3.org/XML/1998/namespace',
    'tei': 'http://www.tei-c.org/ns/1.0'}

ID = '{http://www.w3.org/XML/1998/namespace}id'
LANG = '{http://www.w3.org/XML/1998/namespace}lang'

class TEIConverter:
  '''
  Converts a TEI-encoded XML file to RDF based on the CONTRO argumentation model.
  '''

  def __init__(self):
    '''
    Initialize graph and internal state.
    '''
    self.root = None
    self.parent = {}
    self.names = {}
    self.tei_lang = None
    self.text_lang = None
    self.ann_lang = None

    self.g = Graph(bind_namespaces='rdflib')
    self.g.bind('', DATA)
    self.g.bind('arg', ARG)
    self.g.bind('dul', DUL)

    self.g.add((URIRef(BASE), RDF.type, OWL.Ontology))
    self.g.add((URIRef(BASE), OWL.imports, URIRef('https://w3id.org/contro')))


  def convert(self, xml_path, text_lang, ann_lang):
    '''
    Parse the TEI/XML file to populate the RDF graph.
    '''
    self.text_lang = text_lang
    self.ann_lang = ann_lang

    # Open TEI file
    tree = ET.parse(xml_path)
    self.root = tree.getroot()

    # Pre-compute a parent lookup, mapping each element to its parent
    self.parent = {child: parent for parent in self.root.iter() for child in parent}

    # Dictionary of analysis ids to property names: { 'premise': 'Premise' }
    self.names = {
      el.get(ID): el.text.strip() if el.text else ''
      for el in self.root.findall(".//tei:interp", NS)
    }

    for topic in self.root.findall('.//tei:interpGrp[@xml:id="topic"]/tei:interp', NS):
      self.add_topic(topic)

    # Arguments
    for note in self.root.findall(".//tei:note[@type='paraphrase']", NS):

      # Get ancestor div with responsability info
      ancestor = self.parent.get(note)
      while ancestor is not None and 'resp' not in ancestor.attrib:
        ancestor = self.parent.get(ancestor)

      author_id = ancestor.get('resp')[1:] if ancestor is not None else None
      if author_id:
        author = self.root.find(f".//tei:person[@xml:id='{author_id}']", NS)
        if author is None:
          author = self.root.find(f".//tei:persona[@xml:id='{author_id}']/..", NS)
      if author is not None:
        self.add_person(author)

      for arg in note.findall("./tei:list[@type='syllogism']", NS):
        self.add_argument(arg, author_id)

  def to_turtle(self, ttl_path):
    '''
    Serialize the RDF graph to Turtle format.
    '''
    write_if_changed(self.g.serialize(format='turtle'), ttl_path)

  def get_lang(self, el):
    '''
    Return the xml:lang of the closest ancestor <div> or fallback to TEI or default language.
    '''
    DIV = '{http://www.tei-c.org/ns/1.0}div'
    TEI = '{http://www.tei-c.org/ns/1.0}TEI'

    while el in self.parent:
      el = self.parent[el]
      if el.tag == DIV and LANG in el.attrib:
        return el.get(LANG)
      elif el.tag == TEI:
        if self.tei_lang:
          return self.tei_lang
        tei_lang = el.find('.//tei:textLang', NS).get('mainLang')
        if tei_lang:
          self.tei_lang = tei_lang
          return tei_lang
    return self.text_lang

  def add_topic(self, topic):
    '''
    Add a topic individual and its occurrences to the graph.
    '''
    top_id = topic.get(ID)
    top_uri = DATA[top_id]
    top_lang = topic.get(LANG) or self.ann_lang

    self.g.add((top_uri, RDF.type, OWL.NamedIndividual))
    self.g.add((top_uri, RDFS.label, Literal(self.names[top_id], lang=top_lang)))
    for desc in topic.findall('./tei:desc', NS):
      self.g.add((top_uri, RDFS.comment, Literal(desc.text, lang=top_lang)))

    # Topic instances
    instances = self.root.findall(f".//tei:seg[@ana='#{top_id}']", NS)

    if instances:
      self.g.add((top_uri, RDF.type, DUL.Collection))

    for ins in instances:
      ins_id = ins.get(ID)

      if not ins_id:
        continue
      
      ins_uri = DATA[ins_id]
      self.g.add((ins_uri, RDF.type, OWL.NamedIndividual))
      self.g.add((top_uri, DUL.hasMember, ins_uri))
      self.g.add((ins_uri, PROV.value, Literal(ins.text, lang=self.get_lang(ins))))

  def add_person(self, person):
    '''
    Add a person and their argumentation theory and knowledge base to the graph.
    '''
    person_uri = DATA[person.get(ID)]

    if (person_uri, RDF.type, OWL.NamedIndividual) in self.g:
      return # Already in graph

    self.g.add((person_uri, RDF.type, OWL.NamedIndividual))
    self.g.add((person_uri, RDF.type, DUL.Agent))
    self.g.add((person_uri, OWL.sameAs, URIRef(person.get('sameAs'))))
    self.g.add((person_uri, RDFS.label, Literal(person.find('./tei:persName', NS).text)))

    # Author's Argumentation Theory
    theory_uri = DATA['AT_' + person.get(ID)]
    self.g.add((theory_uri, RDF.type, OWL.NamedIndividual))
    self.g.add((theory_uri, RDF.type, ARG.ArgumentationTheory))
    self.g.add((theory_uri, ARG.DialogicalAgent, person_uri))

    # Author's Knowledge Base
    knowledge_uri = DATA['KB_' + person.get(ID)]
    self.g.add((knowledge_uri, RDF.type, OWL.NamedIndividual))
    self.g.add((knowledge_uri, RDF.type, ARG.KnowledgeBase))
    self.g.add((theory_uri, ARG.KnowledgeBase, knowledge_uri))

    for persona in person.findall('./tei:persona', NS):
      persona_uri = DATA[persona.get(ID)]
      self.g.add((persona_uri, RDF.type, OWL.NamedIndividual))
      self.g.add((persona_uri, RDF.type, DUL.Agent))
      self.g.add((persona_uri, RDFS.label, Literal(persona.find('./tei:persName', NS).text)))
      note = persona.find('./tei:note', NS)
      if note is not None:
        self.g.add((persona_uri, RDFS.comment, Literal(note.text, lang=self.ann_lang)))
      self.g.add((persona_uri, ARG.isAliasOf, person_uri))


  def add_argument(self, arg, author_id):
    '''
    Add an argument and its components to the graph.
    '''
    arg_id = arg.get(ID)
    arg_uri = DATA[arg_id]
    self.g.add((arg_uri, RDF.type, OWL.NamedIndividual))
    self.g.add((arg_uri, RDF.type, ARG.Argument))
    self.g.add((arg_uri, ARG.by, DATA[author_id]))
    self.g.add((arg_uri, ARG.Topic, DATA[arg.get('ana')[1:]]))

    for stmt in arg.findall('./tei:item', NS):
      # If the statement has no id, it is a reference to another statement
      if not stmt.get(ID):
        stmt_uri = DATA[stmt.find('./tei:ptr', NS).get('target')[1:]]
        self.g.add((arg_uri, ARG[self.names[stmt.get('ana')[1:]]], stmt_uri))
        continue

      stmt_id = stmt.get(ID)
      stmt_uri = DATA[stmt_id]
      self.g.add((stmt_uri, RDF.type, OWL.NamedIndividual))
      self.g.add((arg_uri, ARG[self.names[stmt.get('ana')[1:]]], stmt_uri))
      self.g.add((stmt_uri, RDFS.comment, Literal(stmt.text, lang=self.ann_lang)))

      # Inference Rule components (if any)
      antecedents = stmt.get('synch')
      if antecedents:
        for antecedent in antecedents.split():
          self.g.add((stmt_uri, ARG.Antecedent, DATA[antecedent[1:]]))
        self.g.add((stmt_uri, ARG.Consequent, DATA[stmt.get('next')[1:]]))

      # Contrary
      contrary = stmt.get('exclude')
      if contrary:
        self.g.add((stmt_uri, ARG.contradicts, DATA[contrary[1:]]))
      
      # Text content
      for text in self.root.findall(f".//*[@ana='#{stmt_id}']", NS):
        self.preprocess_text(text)
        text_lang = self.get_lang(text)
        full_text = ''.join(text.itertext()).strip()
        self.g.add((stmt_uri, PROV.value, Literal(full_text, lang=text_lang)))


  def preprocess_text(self, el):
    '''
    Wrap <q> content in quotation marks and remove <bibl> before extracting text.
    '''
    for q in el.findall(".//tei:q", NS):
      if q.text:
        q.text = f'«{q.text}»'

    # Remove <bibl>
    for bibl in el.findall(".//tei:bibl", NS):
      parent = self.parent.get(bibl)
      if parent is not None:
        parent.remove(bibl)

def main():
  '''
  Command-line interface to run the TEI to RDF conversion.
  '''
  parser = argparse.ArgumentParser(description='Extract CONTRO entities from an XML/TEI file')
  parser.add_argument('xml_path', help='path to the input .xml file')
  parser.add_argument('ttl_path', help='path to the output .ttl file')
  parser.add_argument(
      '--text',
      nargs='?',
      default='en',
      help='language of the text, default is "en"'
  )
  parser.add_argument(
      '--ann',
      nargs='?',
      default='en',
      help='language of annotations, default is "en"'
  )

  args = parser.parse_args()
  converter = TEIConverter()
  converter.convert(args.xml_path, args.text, args.ann)
  converter.to_turtle(args.ttl_path)


if __name__ == '__main__':
  main()

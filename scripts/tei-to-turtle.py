import argparse

import xml.etree.ElementTree as ET
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS, PROV, OWL

import write_if_changed

BASE = 'https://w3id.org/contro/data'

def main():
  parser = argparse.ArgumentParser(description='Extract CONTRO entities from a XML-TEI file.')
  parser.add_argument('ttl_path', help='Path to the output .ttl file.')
  parser.add_argument('xml_paths', nargs='+', help='Paths to the input .xml files.')

  args = parser.parse_args()

  # RDF namespaces
  ARG = Namespace('https://w3id.org/contro/arg#')
  DATA = Namespace(BASE + '#')
  DUL = Namespace('http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#')
  g = Graph(bind_namespaces='rdflib')
  g.bind('', DATA)
  g.bind('arg', ARG)
  g.bind('dul', DUL)

  g.add((URIRef(BASE), RDF.type, OWL.Ontology))
  g.add((URIRef(BASE), OWL.imports, URIRef('https://w3id.org/contro')))

  # XML namespaces
  ns = {'xml': 'http://www.w3.org/XML/1998/namespace',
      'tei': 'http://www.tei-c.org/ns/1.0'}
  id = '{http://www.w3.org/XML/1998/namespace}id'
  lang = '{http://www.w3.org/XML/1998/namespace}lang'

  for xml_path in args.xml_paths:
    # Open TEI XML
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Pre-compute a parent lookup, mapping each element to its parent
    par = {child: parent for parent in root.iter() for child in parent}

    # Find the closest ancestor div with xml:lang
    def get_lang(el):
      while el in par:
        el = par[el] # El is now the parent
        if el.tag == '{http://www.tei-c.org/ns/1.0}div' and lang in el.attrib:
          return el.get(lang)
      return 'it'

    cat_xpath = './/tei:taxonomy[@xml:id="{}"]/tei:category'

    # Dictionary of category ids to property names
    # e.g. { 'premise': 'Premise' }
    tx = {cat.get(id): cat.find('tei:catDesc', ns).text for cat in root.findall(cat_xpath.format('statement'), ns)}

    # Topics
    for topic in root.findall(cat_xpath.format('topic'), ns):
      topic_id = topic.get(id)
      topic_uri = DATA[topic_id]

      g.add((topic_uri, RDF.type, OWL.NamedIndividual))

      descs = topic.findall('tei:catDesc', ns)
      langs = {desc.get(lang) for desc in descs if desc.get(lang)}

      if langs:
        for l in langs:
          lang_descs = filter(lambda x: x.get(lang) == l, descs)
          topic_title = next(lang_descs).text
          g.add((topic_uri, RDFS.label, Literal(topic_title, lang=l)))
          for topic_desc in lang_descs:
            g.add((topic_uri, RDFS.comment, Literal(topic_desc.text, lang=l)))
      else:
        topic_title = descs[0].text
        g.add((topic_uri, RDFS.label, Literal(topic_title, lang='en')))
        for topic_desc in descs[1:]:
          g.add((topic_uri, RDFS.comment, Literal(topic_desc.text, lang='en')))

      # Topic instances
      instances = root.findall(f".//tei:seg[@ana='#{topic_id}']", ns)

      if instances:
        g.add((topic_uri, RDF.type, DUL.Collection))

      for instance in instances:
        instance_id = instance.get(id)

        if not instance_id:
          continue
        
        instance_uri = DATA[instance_id]
        g.add((instance_uri, RDF.type, OWL.NamedIndividual))
        g.add((topic_uri, DUL.hasMember, instance_uri))
        g.add((instance_uri, PROV.value, Literal(instance.text)))

    # Authors
    def add_person_details(target_id):
      target = root.find(f".//tei:particDesc//tei:person[@xml:id='{target_id}']", ns)
      if target is None:
        person = root.find(f".//tei:particDesc//tei:persona[@xml:id='{target_id}']/..", ns)
      else:
        person = target
      person_uri = DATA[person.get(id)]
      g.add((person_uri, RDF.type, OWL.NamedIndividual))
      g.add((person_uri, RDF.type, DUL.Agent))
      g.add((person_uri, OWL.sameAs, URIRef(person.get('sameAs'))))
      g.add((person_uri, RDFS.label, Literal(person.find('tei:persName', ns).text)))

      # Author's Argumentation Theory
      theory_uri = DATA['AT_' + person.get(id)]
      g.add((theory_uri, RDF.type, OWL.NamedIndividual))
      g.add((theory_uri, RDF.type, ARG.ArgumentationTheory))
      g.add((theory_uri, ARG.DialogicalAgent, person_uri))

      # Author's Knowledge Base
      knowledge_uri = DATA['KB_' + person.get(id)]
      g.add((knowledge_uri, RDF.type, OWL.NamedIndividual))
      g.add((knowledge_uri, RDF.type, ARG.KnowledgeBase))
      g.add((theory_uri, ARG.KnowledgeBase, knowledge_uri))

      for persona in person.findall('tei:persona', ns):
        persona_uri = DATA[persona.get(id)]
        g.add((persona_uri, RDF.type, OWL.NamedIndividual))
        g.add((persona_uri, RDF.type, DUL.Agent))
        g.add((persona_uri, RDFS.label, Literal(persona.find('tei:persName', ns).text)))
        note = persona.find('tei:note', ns)
        if note is not None:
          g.add((persona_uri, RDFS.comment, Literal(note.text, lang='en')))
        g.add((persona_uri, ARG.isAliasOf, person_uri))

    # Arguments
    for note in root.findall(".//tei:note[@type='paraphrase']", ns):

      # Get ancestor div with responsability info
      ancestor = par.get(note)
      while ancestor is not None and 'resp' not in ancestor.attrib:
        ancestor = par.get(ancestor)

      author = ancestor.get('resp')[1:] if ancestor is not None else None

      for arg in note.findall("./tei:list[@type='syllogism']", ns):
        arg_id = arg.get(id)
        arg_uri = DATA[arg_id]
        g.add((arg_uri, RDF.type, OWL.NamedIndividual))
        g.add((arg_uri, RDF.type, ARG.Argument))
        g.add((arg_uri, ARG.by, DATA[author]))
        add_person_details(author)
        g.add((arg_uri, ARG.Topic, DATA[arg.get('ana')[1:]]))

        for stmt in arg.findall('tei:item', ns):
          # If the statement has no id, it is a reference to another statement
          if not stmt.get(id):
            stmt_uri = DATA[stmt.find('tei:ptr', ns).get('target')[1:]]
            g.add((arg_uri, ARG[tx[stmt.get('ana')[1:]]], stmt_uri))
            continue

          stmt_id = stmt.get(id)
          stmt_uri = DATA[stmt_id]
          g.add((stmt_uri, RDF.type, OWL.NamedIndividual))
          g.add((arg_uri, ARG[tx[stmt.get('ana')[1:]]], stmt_uri))
          g.add((stmt_uri, RDFS.comment, Literal(stmt.text, lang='en')))

          # Inference Rule components (if any)
          antecedents = stmt.get('synch')
          if antecedents:
            for antecedent in antecedents.split():
              g.add((stmt_uri, ARG.Antecedent, DATA[antecedent[1:]]))
            g.add((stmt_uri, ARG.Consequent, DATA[stmt.get('next')[1:]]))

          # Contrary
          contrary = stmt.get('exclude')
          if contrary:
            g.add((stmt_uri, ARG.contradicts, DATA[contrary[1:]]))
          
          # Text content
          for text in root.findall(f".//*[@ana='#{stmt_id}']", ns):
            text_lang = get_lang(text)
            full_text = ''.join(text.itertext()).strip()
            g.add((stmt_uri, PROV.value, Literal(full_text, lang=text_lang)))

  write_if_changed(g.serialize(format='turtle'), args.ttl_path)


if __name__ == '__main__':
  main()
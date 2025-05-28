import os
import argparse
import xml.etree.ElementTree as ET
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS, PROV, OWL

def write_if_changed(new, path):
  if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
      old = f.read()
    if old == new:
      return False
  with open(path, 'w', encoding='utf-8') as f:
    f.write(new)
  return True

def main():
  parser = argparse.ArgumentParser(description='Extract CONTRO entities from a XML-TEI file.')
  parser.add_argument('xml_path', help='Path to the input .xml file.')
  parser.add_argument('ttl_path', help='Path to the output .ttl file.')

  args = parser.parse_args()

  # RDF namespaces
  ARG = Namespace('https://w3id.org/contro/arg#')
  CONTRO = Namespace('https://w3id.org/contro/data#')
  DUL = Namespace('http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#')
  g = Graph(bind_namespaces='rdflib')
  g.bind('contro', CONTRO)
  g.bind('arg', ARG)
  g.bind('dul', DUL)

  # Open the ontology
  g.parse(args.ttl_path, format='turtle')

  # XML namespaces
  ns = {'xml': 'http://www.w3.org/XML/1998/namespace',
      'tei': 'http://www.tei-c.org/ns/1.0'}
  id = '{http://www.w3.org/XML/1998/namespace}id'
  lang = '{http://www.w3.org/XML/1998/namespace}lang'

  # Open TEI XML
  tree = ET.parse(args.xml_path)
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
    topic_uri = CONTRO[topic_id]

    g.add((topic_uri, RDF.type, ARG.Topic))

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
      
      instance_uri = CONTRO[instance_id]
      g.add((topic_uri, DUL.hasMember, instance_uri))
      g.add((instance_uri, RDFS.label, Literal(instance.text, lang='it')))

  # Authors
  def add_person_details(target_id):
    target = root.find(f".//tei:particDesc//tei:person[@xml:id='{target_id}']", ns)
    if target is None:
      person = root.find(f".//tei:particDesc//tei:persona[@xml:id='{target_id}']/..", ns)
    else:
      person = target
    person_uri = CONTRO[person.get(id)]
    g.add((person_uri, RDF.type, DUL.Agent))
    g.add((person_uri, OWL.sameAs, URIRef(person.get('sameAs'))))
    g.add((person_uri, RDFS.label, Literal(person.find('tei:persName', ns).text)))

    for persona in person.findall('tei:persona', ns):
      persona_uri = CONTRO[persona.get(id)]
      g.add((persona_uri, RDF.type, DUL.Agent))
      g.add((persona_uri, RDFS.label, Literal(persona.find('tei:persName', ns).text)))
      note = persona.find('tei:note', ns)
      if note is not None:
        g.add((persona_uri, RDFS.comment, Literal(note.text, lang='en')))
      g.add((persona_uri, ARG.personaOf, person_uri))

  # Arguments
  for context in root.findall(".//tei:note[@type='paraphrase']/..", ns): # Get parent div with responsability info
    author = context.get('resp')[1:]

    for arg in context.findall("./tei:note[@type='paraphrase']/tei:list[@type='syllogism']", ns):
      arg_id = arg.get(id)
      arg_uri = CONTRO[arg_id]
      g.add((arg_uri, RDF.type, ARG.Argument))
      g.add((arg_uri, ARG.Author, CONTRO[author]))
      add_person_details(author)
      g.add((arg_uri, ARG.Topic, CONTRO[arg.get('ana')[1:]]))

      for stmt in arg.findall('tei:item', ns):
        # If the statement has no id, it is a reference to another statement
        if not stmt.get(id):
          stmt_uri = CONTRO[stmt.find('tei:ptr', ns).get('target')[1:]]
          g.add((arg_uri, ARG[tx[stmt.get('ana')[1:]]], stmt_uri))
          continue

        stmt_id = stmt.get(id)
        stmt_uri = CONTRO[stmt_id]
        g.add((arg_uri, ARG[tx[stmt.get('ana')[1:]]], stmt_uri))
        g.add((stmt_uri, RDF.type, ARG.Statement))
        g.add((stmt_uri, RDFS.label, Literal(stmt.text, lang='en')))

        # Inference Rule components (if any)
        antecedents = stmt.get('synch')
        if antecedents:
          for antecedent in antecedents.split():
            g.add((stmt_uri, ARG.Antecedent, CONTRO[antecedent[1:]]))
          g.add((stmt_uri, ARG.Consequent, CONTRO[stmt.get('next')[1:]]))

        # Contrary
        contrary = stmt.get('exclude')
        if contrary:
          g.add((stmt_uri, ARG.contradicts, CONTRO[contrary[1:]]))
        
        # Text content
        for text in root.findall(f".//*[@ana='#{stmt_id}']", ns):
          text_lang = get_lang(text)
          full_text = ''.join(text.itertext()).strip()
          g.add((stmt_uri, PROV.value, Literal(full_text, lang=text_lang)))

  write_if_changed(g.serialize(format='turtle'), args.ttl_path)


if __name__ == '__main__':
  main()
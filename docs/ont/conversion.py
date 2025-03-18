from rdflib import Graph, Namespace, URIRef, RDF
import xml.etree.ElementTree as ET

# Define the namespaces
ARG = Namespace("https://w3id.org/contro/arg#")
RDF_NS = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

# Initialize RDF Graph
g = Graph()
g.bind("arg", ARG)
g.bind("rdf", RDF_NS)

# Parse the TEI XML file
tei_xml = """<list type="syllogism"
    xmlns:arg="https://w3id.org/contro/arg#"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <item xml:id="S1" rdf:type="arg:Premise"/>
  <item xml:id="S2" rdf:type="arg:Premise"/>
  <item xml:id="S3" rdf:type="arg:Premise" arg:Antecedent="#S1 #S2" arg:Consequent="#S4"/>
  <item xml:id="S4" rdf:type="arg:Conclusion"/>
</list>"""

# Parse XML
root = ET.fromstring(tei_xml)

# Process each <item>
for item in root.findall("item"):
    item_id = item.get("{http://www.w3.org/XML/1998/namespace}id")  # Get xml:id
    item_uri = URIRef(f"https://w3id.org/contro/arg#{item_id}")  # Create RDF URI

    # Assign rdf:type
    rdf_type = item.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}type")
    if rdf_type:
        g.add((item_uri, RDF.type, URIRef(rdf_type)))

    # Handle Antecedent(s)
    antecedents = item.get("{https://w3id.org/contro/arg#}Antecedent")
    if antecedents:
        for ant in antecedents.split():
            ant_uri = URIRef(f"https://w3id.org/contro/arg#{ant.strip('#')}")
            g.add((item_uri, ARG.Antecedent, ant_uri))

    # Handle Consequent(s)
    consequent = item.get("{https://w3id.org/contro/arg#}Consequent")
    if consequent:
        cons_uri = URIRef(f"https://w3id.org/contro/arg#{consequent.strip('#')}")
        g.add((item_uri, ARG.Consequent, cons_uri))

# Serialize RDF output (Turtle format)
print(g.serialize(format="turtle").decode())

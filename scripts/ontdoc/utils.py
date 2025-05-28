import re
from rdflib import URIRef, RDF, RDFS, OWL


def split_camel_case(s: str) -> str:
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', s)


def is_schema_predicate(p: URIRef) -> bool:
    return (p in RDF) or (p in OWL) or (p in RDFS)
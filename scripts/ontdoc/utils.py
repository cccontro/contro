import re
from urllib.parse import urlparse
from rdflib import URIRef, RDF, RDFS, OWL
from rdflib.namespace import split_uri


def split_camel_case(s: str) -> str:
    return re.sub(r'(?<=[a-z])(?=[A-Z])|_', ' ', s)

def is_schema_predicate(p: URIRef) -> bool:
    return (p in RDF) or (p in OWL) or (p in RDFS)


def get_relative_uri(base: URIRef, uri: URIRef, suffix: str) -> str:
    base_parts = urlparse(str(base))
    uri_parts = urlparse(str(uri))
    base_path = base_parts.path.rstrip('/').split('/')
    uri_path = uri_parts.path.rstrip('/').split('/')

    if not (base_parts.scheme == uri_parts.scheme and base_parts.netloc == uri_parts.netloc and base_path[0] == uri_path[0]):
        return str(uri)

    while base_path and uri_path and base_path[0] == uri_path[0]:
        base_path.pop(0)
        uri_path.pop(0)

    levels = ['..'] * len(base_path)
    rel_dir = '/'.join(levels + uri_path)

    if rel_dir:
        return f"{rel_dir}/#{uri_parts.fragment}_{suffix}"
    else:
        return f"#{uri_parts.fragment}_{suffix}"
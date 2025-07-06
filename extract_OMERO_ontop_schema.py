from shexer.shaper import Shaper
from shexer.consts import TURTLE, MIXED_INSTANCES, ALL_EXAMPLES

import os
namespaces_dict = {
    "http://purl.org/dc/terms/": "dc",
    "http://rdfs.org/ns/void#": "void",
    "http://www.w3.org/2001/XMLSchema#": "xsd",
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
    "http://purl.org/pav/": "pav",
    "http://www.w3.org/ns/dcat#": "dcat",
    "http://xmlns.com/foaf/0.1/": "foaf",
    "http://www.w3.org/2002/07/owl#": "owl",
    "http://www.w3.org/2000/01/rdf-schema#": "rdfs",
    "http://www.w3.org/2004/02/skos/core#": "skos",
}

def run(target_dir, path_to_file, namespaces):
    with open(path_to_file, "r", encoding="utf-8") as f:
        raw_graph = f.read()

    shaper = Shaper(
        raw_graph=raw_graph,
        all_classes_mode=True,
        input_format=TURTLE,
        namespaces_dict=namespaces,
        disable_exact_cardinality=False,
        detect_minimal_iri=True,
        examples_mode=ALL_EXAMPLES,
        instances_report_mode=MIXED_INSTANCES
    )

    result = shaper.shex_graph(
        rdfconfig_directory=target_dir,
        verbose=True,
        acceptance_threshold=0,
        string_output=True
    )

    print(result)

if __name__ == "__main__":
    # Replace 'example.ttl' with the path to your RDF Turtle file
    run(
        target_dir="rdf_config",
        path_to_file="./data/omerordf.ttl",
        namespaces=namespaces_dict
    )
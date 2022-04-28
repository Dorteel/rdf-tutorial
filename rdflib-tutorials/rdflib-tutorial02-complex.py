import rdflib
from rdflib import Graph, Literal, RDF, URIRef
# rdflib knows about quite a few popular namespaces, like W3C ontologies, schema.org etc.
from rdflib.namespace import FOAF , XSD

# Create a Graph and parse in an RDF file hosted on the Internet
somaURL = "https://ease-crc.github.io/soma/owl/current/SOMA.owl#"
bfoURL = "https://raw.githubusercontent.com/BFO-ontology/BFO/v2019-08-26/bfo_classes_only.owl"

# Namespaces
somaNS = "http://www.ease-crc.org/ont/SOMA.owl#"
dulNS = "http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#"

g = Graph().parse(bfoURL)
g.bind('soma', URIRef(somaNS))
g.bind('dul', dulNS)
# Loop through each triple in the graph (subj, pred, obj)
for subj, pred, obj in g:
    print(subj, pred, obj)

# Print the number of "triples" in the Graph
print(f"Graph g has {len(g)} statements.")
# Prints: Graph g has 86 statements.

## Print out the entire Graph in the RDF Turtle format
print(g.serialize(format="turtle"))
from rdflib import Graph

# Create a Graph, pare in Internet data
soma = Graph().parse("https://ease-crc.github.io/soma/owl/current/SOMA.owl")
#dul = Graph().parse("http://www.ontologydesignpatterns.org/ont/dul/DUL.owl")

# Query the data in g using SPARQL
# This query returns the 'name' of all ``foaf:Person`` instances
q = """
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>

    SELECT ?name
    WHERE {
        ?p rdf:type foaf:Person .

        ?p foaf:name ?name .
    }
"""

# Apply the query to the graph and iterate through results
for r in soma.query(q):
    print(r)
    print(r["name"])

# prints: Timothy Berners-Lee
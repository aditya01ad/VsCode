from itertools import product

def HammingGraph(d, q):
    # vertices = all d-tuples over {0,...,q-1}
    vertices = list(product(range(q), repeat=d))

    # create empty graph
    G = Graph(multiedges=False, loops=False)
    G.add_vertices(vertices)

    # add edges: differ in exactly one coordinate
    for i, u in enumerate(vertices):
        for v in vertices[i+1:]:
            diff = sum(1 for j in range(d) if u[j] != v[j])
            if diff == 1:
                G.add_edge(u, v)

    return G

# Example: H(3,3)
# Example: H(3,3)
G = HammingGraph(3, 3)

G.plot()


#print("Graph saved as HammingGraph_3_3.png")


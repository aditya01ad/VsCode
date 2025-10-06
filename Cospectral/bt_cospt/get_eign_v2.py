#!/usr/bin/env python3
"""
Usage:
    python graph_eigenvalues.py
Prompts for n, then edges in Python list format, e.g.
[(0,1), (1,2), (2,0)]
"""
import ast
import numpy as np
import networkx as nx


def main() -> None:
    n = int(input("Number of vertices n: ").strip())
    edges = ast.literal_eval(input("Enter edge list (Python pairs): ").strip())

    G = nx.Graph()
    G.add_nodes_from(range(n))   # ensure 0..n-1 are present
    G.add_edges_from(edges)

    A = nx.to_numpy_array(G)
    eig = np.linalg.eigvalsh(A)
    print("Adjacency eigenvalues (rounded to 6 decimals):")
    print(np.round(eig, 6))


if __name__ == "__main__":
    main()

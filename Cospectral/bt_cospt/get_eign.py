#!/usr/bin/env python3
"""
Usage:
    python graph_eigenvalues.py
Then type the edges one per line, blank line to finish.
Example input:
    0 1
    1 2
    2 0
    <blank line>
"""
import numpy as np
import networkx as nx


def read_graph() -> nx.Graph:
    G = nx.Graph()
    print("Enter edges as 'u v' (one per line), empty line to finish:")
    while True:
        line = input().strip()
        if not line:
            break
        u, v = map(int, line.split())
        G.add_edge(u, v)
    return G


def main() -> None:
    G = read_graph()
    A = nx.to_numpy_array(G)
    eig = np.linalg.eigvalsh(A)
    print("Adjacency eigenvalues (rounded to 6 decimals):")
    print(np.round(eig, 6))


if __name__ == "__main__":
    main()

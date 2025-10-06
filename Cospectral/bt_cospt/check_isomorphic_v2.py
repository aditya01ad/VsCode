#!/usr/bin/env python3
"""
Usage:
    python graph_isomorphic.py
Prompts for n1, edges-1, n2, edges-2.
"""
import ast
import networkx as nx


def read_one_graph(name: str) -> nx.Graph:
    n = int(input(f"Number of vertices for {name}: ").strip())
    edges = ast.literal_eval(
        input(f"Enter edge list for {name} (Python pairs): ").strip()
    )
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(edges)
    return G


def main() -> None:
    G1 = read_one_graph("graph-1")
    G2 = read_one_graph("graph-2")

    if nx.is_isomorphic(G1, G2):
        print("-> The two graphs ARE isomorphic.")
    else:
        print("-> The two graphs are NOT isomorphic.")


if __name__ == "__main__":
    main()

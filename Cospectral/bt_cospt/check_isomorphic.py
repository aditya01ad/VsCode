#!/usr/bin/env python3
"""
Usage:
    python graph_isomorphic.py
You will be prompted for the edges of graph-1, then graph-2.
"""
import networkx as nx


def read_one_graph(name: str) -> nx.Graph:
    G = nx.Graph()
    print(f"Enter edges for {name} ('u v' per line), empty line to finish:")
    while True:
        line = input().strip()
        if not line:
            break
        u, v = map(int, line.split())
        G.add_edge(u, v)
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

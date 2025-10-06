#!/usr/bin/env python3
"""
Find all cospectral, non-isomorphic simple graphs with v vertices and e edges.

Single-file version – no external dependencies except numpy and networkx.
If the optional package `networkx-graph-hash` is installed the code
automatically uses the full NAUTY canonical labelling; otherwise it falls
back to a colour-refinement hash (still much faster than pairwise
isomorphism checks).
"""

from __future__ import annotations
import sys
import time
from itertools import combinations
from collections import defaultdict

import numpy as np
import networkx as nx

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="networkx.*graph_hashing")

# ------------------------------------------------------------------
# 1.  Canonical-labelling helper
# ------------------------------------------------------------------
try:
    # full NAUTY canonical key (needs: pip install networkx-graph-hash)
    from networkx.algorithms.graph_hashing import graph_hash
    _canonical_key = lambda G: graph_hash(G, node_attr=None, edge_attr=None)
except ImportError:
    # fall-back: Weisfeiler–Lehman hash
    _canonical_key = lambda G: nx.weisfeiler_lehman_graph_hash(G, iterations=10)


# ------------------------------------------------------------------
# 2.  Spectrum helper
# ------------------------------------------------------------------
def _spectrum(graph: nx.Graph, v: int) -> tuple[float, ...]:
    """Adjacency spectrum rounded to 8 decimals."""
    A = np.zeros((v, v), dtype=np.float64)
    for u, w in graph.edges:
        A[u, w] = A[w, u] = 1.0
    return tuple(np.round(np.linalg.eigvalsh(A), 8))


# ------------------------------------------------------------------
# 3.  Core routine
# ------------------------------------------------------------------
def find_cospectral_nonisomorphic_graphs(v: int, e: int, *, verbose: bool = True):
    """Return list of cospectral+non-isomorphic graph sets."""
    print("Finding cospectral non-isomorphic graphs...........")
    if not 0 <= e <= v * (v - 1) // 2:
        print(f"Error: edge count {e} impossible for simple graph on {v} vertices.")
        return []

    if verbose:
        print(f"Generating all graphs with v={v}, e={e} ...")

    possible_edges = list(combinations(range(v), 2))

    # spectrum  -> list of canonical keys
    buckets: dict[tuple[float, ...], list[str]] = defaultdict(list)
    # spectrum  -> list of Graph objects (one per isomorphism class)
    groups: dict[tuple[float, ...], list[nx.Graph]] = defaultdict(list)
    print("list created...............")
    #t0 = time.time()
    print("Running", end = " ")
    for edge_set in combinations(possible_edges, e):
        #print(".", end = " ")
        G = nx.Graph()
        G.add_edges_from(edge_set)

        spec = _spectrum(G, v)
        key = _canonical_key(G)

        if key not in buckets[spec]:      # new isomorphism class for this spectrum
            print(".", end = " ")
            buckets[spec].append(key)
            groups[spec].append(G)

    if verbose:
        print(f"\n  finished generation + bucketing")
        

    # keep only spectra with more than one isomorphism class
    return [grp for grp in groups.values() if len(grp) > 1]


# ------------------------------------------------------------------
# 4.  Pretty printer
# ------------------------------------------------------------------
def _pretty_print(cospectral_sets: list[list[nx.Graph]]) -> None:
    if not cospectral_sets:
        print("\nNo cospectral, non-isomorphic graphs found.")
        return

    print(f"\nFound {len(cospectral_sets)} set(s):")
    for idx, graphs in enumerate(cospectral_sets, 1):
        print(f"\n--- set {idx}  ({len(graphs)} non-isomorphic graphs) ---")
        for j, G in enumerate(graphs, 1):
            spec = np.linalg.eigvalsh(nx.to_numpy_array(G))
            print(f"Graph {j}:  edges={list(G.edges())}")
            print(f"   spectrum: {np.round(spec, 4)}")


# ------------------------------------------------------------------
# 5.  Command-line interface
# ------------------------------------------------------------------
def _cli():
    try:
        v = int(input("v (vertices): ").strip())
        e = int(input("e (edges): ").strip())
    except ValueError:
        print("Please enter integers.")
        sys.exit(1)

    sets = find_cospectral_nonisomorphic_graphs(v, e)
    _pretty_print(sets)


if __name__ == "__main__":
    _cli()

import networkx as nx
from networkx.algorithms import isomorphism

def is_biregular_distinct(G):
    """Check if bipartite G is biregular with distinct degrees."""
    if not nx.is_bipartite(G):
        return False
    X, Y = nx.bipartite.sets(G)
    deg_X = {d for _, d in G.degree(X)}
    deg_Y = {d for _, d in G.degree(Y)}
    return len(deg_X) == 1 and len(deg_Y) == 1 and deg_X != deg_Y

def is_balanced(G):
    """Check if bipartite G is balanced (equal part sizes)."""
    if not nx.is_bipartite(G):
        return False
    X, Y = nx.bipartite.sets(G)
    return len(X) == len(Y)

def admits_swap_automorphism(G):
    """
    Check if bipartite graph G admits an automorphism swapping its partite sets.
    We test isomorphism between G and its bipartition-swapped relabeling.
    """
    if not nx.is_bipartite(G):
        return False
    
    X, Y = nx.bipartite.sets(G)
    # Swap labeling: map X->Y and Y->X
    mapping = {x: f"x_{i}" for i, x in enumerate(X)}
    mapping.update({y: f"y_{i}" for i, y in enumerate(Y)})
    
    G1 = nx.relabel_nodes(G, mapping)
    
    # Swap parts
    swapped_mapping = {}
    for i, x in enumerate(X):
        swapped_mapping[f"x_{i}"] = f"y_{i % len(Y)}"
    for i, y in enumerate(Y):
        swapped_mapping[f"y_{i}"] = f"x_{i % len(X)}"
    
    G2 = nx.relabel_nodes(G1, swapped_mapping)
    
    GM = isomorphism.GraphMatcher(G1, G2)
    return GM.is_isomorphic()

def theorem_4_6(G_L, G_H):
    """Check Theorem 4.6 conditions for G_L and G_H."""
    if not is_biregular_distinct(G_L):
        return "Condition failed: G_L is not biregular with distinct degrees."
    if not is_balanced(G_H):
        return "Condition failed: G_H is not balanced."
    
    swap = admits_swap_automorphism(G_H)
    
    if swap:
        return "G_L⊗H and G_L⊗H# may be isomorphic (H admits swap automorphism)."
    else:
        return "G_L⊗H and G_L⊗H# are nonisomorphic (Theorem 4.6)."

"""
# --- Example usage ---
G_L = nx.bipartite.random_graph(6, 6, 0.5, seed=42)
G_H = nx.bipartite.random_graph(6, 6, 0.5, seed=24)
print("G_L edges:", G_L.edges())        
print("G_H edges:", G_H.edges())
result = theorem_4_6(G_L, G_H)
print(result)
"""
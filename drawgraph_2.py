import networkx as nx
import matplotlib.pyplot as plt

def T_nk(n, k):
    """
    Construct the graph T_{n,k} = K_k ∨ complement(K_{n-k})
    where ∨ denotes the graph join.
    """
    if k >= n or k < 1:
        raise ValueError("Require 1 <= k < n")
    
    # Create the two parts
    Kk = nx.complete_graph(k)               # K_k
    Knk_complement = nx.empty_graph(n - k)  # complement(K_{n-k}) = n-k isolated nodes
    
    # Relabel nodes of the second part to avoid overlap
    Knk_complement = nx.relabel_nodes(Knk_complement, lambda x: x + k)
    
    # Union the two graphs
    G = nx.union(Kk, Knk_complement)
    
    # Add join edges: connect every vertex in K_k to every vertex in complement part
    for u in range(k):              # nodes of K_k
        for v in range(k, n):       # nodes of complement part
            G.add_edge(u, v)
    
    return G

def draw_Tnk(n, k):
    """Draws T_{n,k} graph with labels."""
    G = T_nk(n, k)
    plt.figure(figsize=(5, 5))
    pos = nx.spring_layout(G, seed=42)  # layout for nice visualization
    nx.draw(G, pos, with_labels=True, node_color="skyblue",
            node_size=700, font_size=12, edge_color="gray")
    plt.title(f"T_{{{n},{k}}} Graph", fontsize=14)
    plt.show()

# --- Examples ---
#draw_Tnk(6, 1)   # star S6
#draw_Tnk(6, 2)   # crown with 4 triangles
#draw_Tnk(7, 3)   # pyramid graph

n=15 ; k=7;
draw_Tnk(n, k)
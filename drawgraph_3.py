import networkx as nx
import matplotlib.pyplot as plt

def T_nk(n, k):
    """
    Construct T_{n,k} = K_k ∨ complement(K_{n-k})
    Returns graph G and lists of edge types.
    """
    if k >= n or k < 1:
        raise ValueError("Require 1 <= k < n")
    
    # Create the two parts
    Kk = nx.complete_graph(k)               
    Knk_complement = nx.empty_graph(n - k)  
    
    # Relabel nodes of the second part to avoid overlap
    Knk_complement = nx.relabel_nodes(Knk_complement, lambda x: x + k)
    
    # Union the two graphs
    G = nx.union(Kk, Knk_complement)
    
    # Edge categories
    clique_edges = list(Kk.edges())  # inside K_k
    join_edges = []
    
    # Add join edges: connect every vertex in K_k to every vertex in complement part
    for u in range(k):              
        for v in range(k, n):       
            G.add_edge(u, v)
            join_edges.append((u, v))
    
    return G, clique_edges, join_edges

def draw_Tnk_colored(n, k):
    """Draw T_{n,k} with different colors for clique vs join edges."""
    G, clique_edges, join_edges = T_nk(n, k)
    
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G, seed=42)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=700)
    nx.draw_networkx_labels(G, pos, font_size=12)
    
    # Draw edges with different colors
    nx.draw_networkx_edges(G, pos, edgelist=clique_edges, edge_color="blue", width=2, label="Clique edges")
    nx.draw_networkx_edges(G, pos, edgelist=join_edges, edge_color="red", width=1, label="Join edges")
    
    plt.title(f"T_{{{n},{k}}} Graph (Colored Edges)", fontsize=14)
    plt.legend()
    plt.show()

# --- Examples ---
#draw_Tnk_colored(6, 1)   # star
#draw_Tnk_colored(6, 2)   # crown
#draw_Tnk_colored(7, 3)   # pyramid

n = 5
k = 3
draw_Tnk_colored(n, k)
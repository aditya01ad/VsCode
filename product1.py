import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import eigvals
from product2 import *

# Helper: adjacency spectrum
def adjacency_spectrum(G):
    A = nx.to_numpy_array(G)
    return np.sort(np.real(eigvals(A)))

# Helper: normalized Laplacian spectrum
def norm_laplacian_spectrum(G):
    L = nx.normalized_laplacian_matrix(G).toarray() # .A is deprecated, use .toarray()
    return np.sort(np.real(eigvals(L)))


def draw_graph_product_3(G1, G2, product_type="tensor", layout="spring", cmap="coolwarm"):
    """
    Draw the product of two graphs G1 and G2 with degree-based vertex colors.

    - Vertex colors: proportional to degree (colormap, brighter).
    - Edge colors: light gray.
    """
    # --- Build product graph ---
    if product_type == "tensor":
        G_prod = nx.tensor_product(G1, G2)
    elif product_type == "cartesian":
        G_prod = nx.cartesian_product(G1, G2)
    elif product_type == "strong":
        G_prod = nx.strong_product(G1, G2)
    elif product_type == "lexicographic":
        G_prod = nx.lexicographic_product(G1, G2)
    else:
        raise ValueError("Invalid product_type. Choose from tensor, cartesian, strong, lexicographic.")
    
    # --- Layout ---
    if layout == "spring":
        pos = nx.spring_layout(G_prod, seed=42)
    elif layout == "circular":
        pos = nx.circular_layout(G_prod)
    elif layout == "kamada":
        pos = nx.kamada_kawai_layout(G_prod)
    elif layout == "spectral":
        pos = nx.spectral_layout(G_prod)
    elif layout == "shell":
        pos = nx.shell_layout(G_prod)
    elif layout == "random":
        pos = nx.random_layout(G_prod, seed=42)
    else:
        pos = nx.spring_layout(G_prod, seed=42)
        print("Invalid layout choice. Using spring layout.")
    
    # --- Compute degrees and normalize ---
    degrees = dict(G_prod.degree())
    node_values = list(degrees.values())
    max_deg = max(node_values) if node_values else 1
    node_colors = [deg / max_deg for deg in node_values]
    
    # --- Draw ---
    plt.figure(figsize=(7, 7))
    nodes = nx.draw_networkx_nodes(G_prod, pos,
                                   node_color=node_colors,
                                   cmap=plt.get_cmap(cmap),
                                   node_size=700,
                                   edgecolors="black")
    nx.draw_networkx_edges(G_prod, pos, edge_color="lightgray", width=2)
    nx.draw_networkx_labels(G_prod, pos, font_size=9, font_color="black")
    
    plt.title(f"{product_type.capitalize()} product of G1 and G2 (colored by degree)", fontsize=14)
    plt.colorbar(nodes, ax=plt.gca(), label="Relative degree")
    plt.axis("off")
    plt.show()
    
    return G_prod


def draw_graph_product_2(G1, G2, product_type="tensor", layout="spring"):
    """
    Draw the product of two graphs G1 and G2 with vertex/edge coloring.
    
    Vertex colors: based on first factor (G1).
    Edge colors: based on which relation they come from.
    """
    # --- Build product graph ---
    if product_type == "tensor":
        G_prod = nx.tensor_product(G1, G2)
    elif product_type == "cartesian":
        G_prod = nx.cartesian_product(G1, G2)
    elif product_type == "strong":
        G_prod = nx.strong_product(G1, G2)
    elif product_type == "lexicographic":
        G_prod = nx.lexicographic_product(G1, G2)
    else:
        raise ValueError("Invalid product_type. Choose from tensor, cartesian, strong, lexicographic.")
    
    # --- Layouts ---
    if layout == "spring":
        pos = nx.spring_layout(G_prod, seed=42)
    elif layout == "circular":
        pos = nx.circular_layout(G_prod)
    elif layout == "kamada":
        pos = nx.kamada_kawai_layout(G_prod)
    else:
        pos = nx.spring_layout(G_prod, seed=42)
    
    # --- Vertex colors ---
    # Each node is a tuple (u, v)
    node_colors = []
    for (u, v) in G_prod.nodes():
        node_colors.append(u % 2)  # simple coloring by G1 index (parity)
    
    cmap_nodes = plt.cm.coolwarm
    
    # --- Edge colors ---
    edge_colors = []
    for (u1, v1), (u2, v2) in G_prod.edges():
        if u1 == u2:   # edge came from second graph G2
            edge_colors.append("green")
        elif v1 == v2: # edge came from first graph G1
            edge_colors.append("blue")
        else:          # in strong products, both change
            edge_colors.append("red")
    
    # --- Draw ---
    plt.figure(figsize=(7, 7))
    nx.draw_networkx(G_prod, pos,
                     with_labels=True,
                     node_color=node_colors,
                     cmap=cmap_nodes,
                     edge_color=edge_colors,
                     node_size=600,
                     font_size=8,
                     width=2)
    
    plt.title(f"{product_type.capitalize()} product of G1 and G2", fontsize=14)
    plt.axis("off")
    plt.show()
    
    return G_prod


def draw_graph_product(G1, G2, product_type="tensor", layout="spring"):
    """
    Draw the product of two graphs G1 and G2.
    
    Parameters:
    -----------
    G1, G2 : networkx.Graph
        Input graphs.
    product_type : str
        Type of product: "tensor", "cartesian", "strong", "lexicographic".
    layout : str
        Layout type for visualization: "spring", "circular", "kamada".
    """
    
    # Compute product graph
    if product_type == "tensor":
        G_prod = nx.tensor_product(G1, G2)
    elif product_type == "cartesian":
        G_prod = nx.cartesian_product(G1, G2)
    elif product_type == "strong":
        G_prod = nx.strong_product(G1, G2)
    elif product_type == "lexicographic":
        G_prod = nx.lexicographic_product(G1, G2)
    else:
        raise ValueError("Invalid product_type. Choose from tensor, cartesian, strong, lexicographic.")
    
    # Choose layout
    if layout == "spring":
        pos = nx.spring_layout(G_prod, seed=42)
    elif layout == "circular":
        pos = nx.circular_layout(G_prod)
    elif layout == "kamada":
        pos = nx.kamada_kawai_layout(G_prod)
    else:
        pos = nx.spring_layout(G_prod, seed=42)
    
    # Draw graph
    plt.figure(figsize=(6, 6))
    nx.draw_networkx(G_prod, pos, 
                     with_labels=True, 
                     node_color="skyblue", 
                     node_size=600, 
                     font_size=8, 
                     edge_color="gray")
    
    plt.title(f"{product_type.capitalize()} product of G1 and G2", fontsize=12)
    plt.axis("off")
    plt.show()
    
    return G_prod

import numpy as np

def matrix_product(A, B, product_type="tensor"):
    """
    Compute the adjacency matrix of the product of two graphs (matrix version).
    
    Parameters:
    -----------
    A, B : numpy.ndarray
        Adjacency matrices of the two graphs.
    product_type : str
        One of: "tensor", "cartesian", "strong", "lexicographic".
    
    Returns:
    --------
    numpy.ndarray
        Adjacency matrix of the product graph.
    """
    I_A = np.eye(A.shape[0], dtype=int)
    I_B = np.eye(B.shape[0], dtype=int)
    J_B = np.ones((B.shape[0], B.shape[0]), dtype=int)

    if product_type == "tensor":   # Kronecker product
        return np.kron(A, B)
    
    elif product_type == "cartesian":
        return np.kron(A, I_B) + np.kron(I_A, B)
    
    elif product_type == "strong":
        return np.kron(A, B) + np.kron(A, I_B) + np.kron(I_A, B)
    
    elif product_type == "lexicographic":
        return np.kron(A, J_B) + np.kron(I_A, B)
    
    else:
        raise ValueError("Invalid product_type. Choose from 'tensor', 'cartesian', 'strong', or 'lexicographic'.")

np.set_printoptions(precision=4, suppress=True)
""" # --- Example usage ---
G1 = nx.star_graph(7)  # 3-regular graph on 7 vertices
G2 = nx.cycle_graph(3)
print(matrix_product(nx.to_numpy_array(G1), nx.to_numpy_array(G2), product_type="tensor"))
val1 = theorem_3_1(G1, G2)
val2 = theorem_3_3(G1, G2)

print_spectra(val1)
print_spectra(val2)
#draw_graph_product(G1, G2, product_type="tensor", layout="spring")
"""
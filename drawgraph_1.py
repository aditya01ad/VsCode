import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# --- Define your graph here ---
# Example: a simple graph with 5 vertices and edges
# edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 5), (2, 4)]
# Complete graph with 11 vertices
n= 50
edges = [(i, j) for i in range(1, n+1) for j in range(i + 1, n+1)]


# Create graph
G = nx.Graph()
G.add_edges_from(edges)

# --- Adjacency matrix ---
A = nx.to_numpy_array(G, dtype=int)
print("Adjacency Matrix:\n", A)

# --- Spectrum (Eigenvalues of adjacency matrix) ---
eigenvalues = np.linalg.eigvals(A)
print("\nEigenvalues (Adjacency Spectrum):")
print(np.round(np.sort(eigenvalues)[::-1], 4))  # sorted, rounded


# Draw graph
plt.figure(figsize=(5, 5))
pos = nx.spring_layout(G)  # layout for better visualization
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=700, font_size=12, edge_color="gray")
plt.title("Graph Visualization", fontsize=14)
plt.show()


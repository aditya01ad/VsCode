import networkx as nx
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def hamming_graph(d, q):
    G = nx.Graph()
    vertices = list(itertools.product(range(q), repeat=d))
    G.add_nodes_from(vertices)
    for i, u in enumerate(vertices):
        for v in vertices[i+1:]:
            diff = sum(1 for j in range(d) if u[j] != v[j])
            if diff == 1:
                G.add_edge(u, v)
    return G

q=4
# Example: H(3,2) is a cube
G = hamming_graph(3, q)

# Get 3D coordinates from node labels directly (since tuples are coordinates)
pos = {node: node for node in G.nodes()}

# Plot in 3D
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# Draw edges
for (u, v) in G.edges():
    x = [pos[u][0], pos[v][0]]
    y = [pos[u][1], pos[v][1]]
    z = [pos[u][2], pos[v][2]]
    ax.plot(x, y, z, color='black')

# Draw nodes
xs, ys, zs = zip(*pos.values())
ax.scatter(xs, ys, zs, s=100, c='skyblue', edgecolors='black')

# Label nodes
for node in G.nodes():
    ax.text(pos[node][0], pos[node][1], pos[node][2], str(node), size=10)

ax.set_title("Hamming Graph H(3,2) - Cube")
plt.show()


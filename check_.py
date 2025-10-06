import networkx as nx, numpy as np
n = 7
G = nx.path_graph(n);  
H1 = nx.star_graph(n-1);
H2 = nx.cycle_graph(n);
H3 = nx.wheel_graph(n);

H = H3;
laG = np.linalg.eigvalsh(nx.laplacian_matrix(G).toarray()) # Use .toarray() instead of .A
laH = np.linalg.eigvalsh(nx.laplacian_matrix(H).toarray()) # Use .toarray() instead of .A
print(np.allclose(sorted(laG), sorted(laH)))   # True → cospectral
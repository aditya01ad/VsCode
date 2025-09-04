import networkx as nx
from product2 import *
from product1 import *
from noniso import theorem_4_6


c = "cartesian"
t = "tensor"
s = "strong"
lg = "lexicographic"
product_type = t

sp = "spring"
c = "circular"
k = "kamada"
r = "random"
sh = "shell"
layout = c

G1 = nx.star_graph(4)  # 3-regular graph on 7 vertices
G2 = nx.cycle_graph(3)
G3 = nx.path_graph(4)
G4 = nx.complete_graph(3)
G5 = nx.empty_graph(3)
G6 = nx.wheel_graph(5)
G7 = nx.balanced_tree(2, 2)
G8 = nx.petersen_graph()
G9 = nx.triangular_lattice_graph(2, 2)
G10 = nx.icosahedral_graph()
G11 = nx.dodecahedral_graph()
G12 = nx.tetrahedral_graph()
G13 = nx.octahedral_graph()
G14 = nx.cubical_graph()
G15 = nx.lollipop_graph(3, 3)
G16 = nx.full_rary_tree(3, 2)
G17 = nx.barbell_graph(3, 1)
G18 = nx.random_regular_graph(3, 10, seed=42)
G20 = nx.random_geometric_graph(10, 0.5, seed=42)
G21 = nx.random_lobster(10, 0.5, 0.5, seed=42)
#G22 = nx.random_shell_graph([3, 4, 5], seed=42)
G23 = nx.random_powerlaw_tree(10, 2.5, seed=42)
G24 = nx.bipartite.random_graph(6, 6, 0.5, seed=42)
G25 = nx.bipartite.random_graph(6, 6, 0.5, seed=24)
print(matrix_product(nx.to_numpy_array(G1), nx.to_numpy_array(G2), product_type))

GL = G24
GH = G25
val1 = theorem_3_1(GL, GH)
val2 = theorem_3_3(GL, GH)
val3 = theorem_4_6(GL, GH)

print_spectra(val1)
print_spectra(val2)
print(val3)
draw_graph_product_3(GL, GH, product_type, layout)
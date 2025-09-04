n = 5
Gs = list(graphs(n))
print(len(Gs), "non-isomorphic graphs on", n, "vertices")

G = Gs[0]
print("Spectrum:", G.spectrum())

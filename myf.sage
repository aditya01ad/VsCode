n = 5  # change this (safe up to ~8; 9+ explodes)
gen = graphs(n)          # generator of all non-isomorphic graphs on n vertices
count = sum(1 for _ in gen)
count
n = 5
Gs = list(graphs(n))
len(Gs)    # number of non-isomorphic graphs on n vertices

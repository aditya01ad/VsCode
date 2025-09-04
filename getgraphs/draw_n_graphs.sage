import os

n = 8   # number of vertices
folder = f"graphs_{n}"   # folder name depends on n

# Create the folder if it doesn’t exist
os.makedirs(folder, exist_ok=True)

# Generate all non-isomorphic graphs with n vertices
Gs = list(graphs(n))
print(f"Total non-isomorphic graphs on {n} vertices: {len(Gs)}")

# Draw and save each graph
for i, G in enumerate(Gs):
    P = G.plot()
    filename = os.path.join(folder, f"graph_{n}_{i}.png")
    P.save(filename)
    print(f"Saved {filename}")

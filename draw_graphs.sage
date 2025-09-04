# Number of vertices
n = 4   # change this to your desired n

# Generate all non-isomorphic graphs with n vertices
Gs = list(graphs(n))
print(f"Total non-isomorphic graphs on {n} vertices: {len(Gs)}")

# Draw and save each graph
for i, G in enumerate(Gs):
    P = G.plot()                        # get plot object
    filename = f"graph_{n}_{i}.png"     # unique filename
    P.save(filename)                    # save to file
    print(f"Saved {filename}")

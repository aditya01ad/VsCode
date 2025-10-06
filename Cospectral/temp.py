import networkx as nx
import numpy as np
from itertools import combinations, groupby

def find_cospectral_nonisomorphic_graphs(v, e):
    """
    Generates all simple graphs with 'v' vertices and 'e' edges,
    then groups them by their adjacency spectrum to find cospectral sets.
    Finally, it filters these sets to find non-isomorphic graphs.

    Args:
        v (int): The number of vertices.
        e (int): The number of edges.

    Returns:
        list: A list of lists, where each inner list contains
              networkx Graph objects that are cospectral but
              non-isomorphic to each other.
    """
    print("finding....")
    if not 0 <= e <= v * (v - 1) / 2:
        print(f"Error: Edge count {e} is not possible for a simple graph with {v} vertices.")
        return []

    print(f"Generating all graphs with {v} vertices and {e} edges...")
    
    nodes = range(v)
    possible_edges = combinations(nodes, 2)
    
    # 1. Generate all unique graphs with v nodes and e edges
    all_graphs = [nx.Graph(edge_list) for edge_list in combinations(possible_edges, e)]
    
    # 2. Calculate the spectrum for each graph.
    # We round the eigenvalues and convert to a tuple to make them hashable for grouping.
    def get_spectrum_tuple(G):
        A = nx.to_numpy_array(G)
        eigenvalues = np.linalg.eigvalsh(A)
        return tuple(np.round(eigenvalues, decimals=8))

    # Pair each graph with its spectrum
    print("pairing....")
    graphs_with_spectra = [(G, get_spectrum_tuple(G)) for G in all_graphs]

    # 3. Group graphs by their spectrum
    # Sort by spectrum first to ensure groupby works correctly
    print("shorting......")
    graphs_with_spectra.sort(key=lambda item: item[1])
    
    cospectral_groups = []
    for _, group in groupby(graphs_with_spectra, key=lambda item: item[1]):
        graphs_in_group = [item[0] for item in group]
        if len(graphs_in_group) > 1:
            cospectral_groups.append(graphs_in_group)

    print(f"Found {len(cospectral_groups)} sets of cospectral graphs.")

    # 4. From the cospectral sets, find the non-isomorphic ones
    print("find non-isomorphic.....")
    final_cospectral_nonisomorphic_sets = []
    for group in cospectral_groups:
        unique_nonisomorphic_graphs = []
        if not group:
            continue
        
        # Add the first graph to our list of unique graphs
        unique_nonisomorphic_graphs.append(group[0])
        
        # For each other graph, check if it's isomorphic to any we've already found
        for i in range(1, len(group)):
            is_isomorphic_to_found = False
            for unique_graph in unique_nonisomorphic_graphs:
                if nx.is_isomorphic(group[i], unique_graph):
                    is_isomorphic_to_found = True
                    break
            if not is_isomorphic_to_found:
                unique_nonisomorphic_graphs.append(group[i])
        
        # If we found more than one non-isomorphic graph in the cospectral set
        if len(unique_nonisomorphic_graphs) > 1:
            final_cospectral_nonisomorphic_sets.append(unique_nonisomorphic_graphs)
            
    return final_cospectral_nonisomorphic_sets

# --- Example Usage ---
# Be careful: The number of graphs grows extremely fast.
# v=5, e=6 is a good starting point.
# v=6, e=8 is also manageable.
# v=7, e=10 and above will be very slow.
if __name__ == "__main__":
    num_vertices = int(input(" v :"))
    num_edges = int(input("e :"))
    print("v = ", num_vertices, "e = ", num_edges);
    cospectral_sets = find_cospectral_nonisomorphic_graphs(num_vertices, num_edges)

    if not cospectral_sets:
        print(f"\nNo cospectral, non-isomorphic graphs found for v={num_vertices}, e={num_edges}.")
    else:
        print(f"\nFound {len(cospectral_sets)} set(s) of cospectral, non-isomorphic graphs:")
        for i, s in enumerate(cospectral_sets):
            print(f"\n--- Set {i+1} (found {len(s)} non-isomorphic graphs) ---")
            for j, G in enumerate(s):
                spectrum = np.linalg.eigvalsh(nx.to_numpy_array(G))
                print(f"Graph {j+1}: Edges={list(G.edges())}")
                print(f"  Spectrum: {np.round(spectrum, 4)}")

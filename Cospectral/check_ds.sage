# SageMath code to test if a graph is DS (Determined by Spectrum)

def is_DS(G, verbose=True):
    """
    Check if graph G is determined by its adjacency spectrum.
    Returns True if DS, False otherwise.
    """
    n = G.order()
    spectrum = sorted(G.spectrum())
    
    cospectral_mates = []
    
    # loop over all graphs of same order
    for H in graphs(n):
        if sorted(H.spectrum()) == spectrum:
            if not G.is_isomorphic(H):
                cospectral_mates.append(H)
    
    if cospectral_mates:
        if verbose:
            print(f"Graph on {n} vertices is NOT DS.")
            print(f"Found {len(cospectral_mates)} non-isomorphic cospectral mates.")
        return False
    else:
        if verbose:
            print(f"Graph on {n} vertices IS DS.")
        return True

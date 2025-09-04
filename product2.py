import numpy as np
import networkx as nx
from numpy.linalg import eigvals

# ---------- Helper Spectra ----------
def adjacency_spectrum(G):
    A = nx.to_numpy_array(G, dtype=float)
    return np.sort(np.real(eigvals(A)))

def normalized_laplacian_spectrum(G):
    L = nx.normalized_laplacian_matrix(G).toarray()
    return np.sort(np.real(eigvals(L)))


# ---------- Partitioned Tensor Product ----------
def partitioned_tensor(A, B, transpose_B=False):
    """
    Construct partitioned tensor product of bipartite adjacency matrices.
    
    Parameters:
    -----------
    A : numpy.ndarray (m x n)
    B : numpy.ndarray (p x q)
    transpose_B : bool
        If True, use B^T instead of B (for H#).
    
    Returns:
    --------
    numpy.ndarray
        Adjacency matrix of the product.
    """
    if transpose_B:
        B = B.T
    # Kronecker-type partitioned tensor
    return np.kron(A, np.eye(B.shape[0])) + np.kron(np.eye(A.shape[0]), B)


# ---------- Theorem 3.1 : Adjacency Cospectrality ----------
def theorem_3_1(G_L, G_H):
    """
    Check cospectrality (adjacency matrices) as in Theorem 3.1.
    """
    A_L = nx.to_numpy_array(G_L, dtype=float)
    A_H = nx.to_numpy_array(G_H, dtype=float)
    
    # Partitioned tensor products
    P1 = partitioned_tensor(A_L, A_H, transpose_B=False)
    P2 = partitioned_tensor(A_L, A_H, transpose_B=True)
    
    eig1 = np.sort(np.real(eigvals(P1)))
    eig2 = np.sort(np.real(eigvals(P2)))
    
    return np.allclose(eig1, eig2), eig1, eig2


# ---------- Theorem 3.3 : Normalized Laplacian Cospectrality ----------
def theorem_3_3(G_L, G_H):
    """
    Check cospectrality (normalized Laplacian) as in Theorem 3.3.
    """
    L_L = nx.normalized_laplacian_matrix(G_L).toarray()
    L_H = nx.normalized_laplacian_matrix(G_H).toarray()
    
    # Partitioned tensor products
    P1 = partitioned_tensor(L_L, L_H, transpose_B=False)
    P2 = partitioned_tensor(L_L, L_H, transpose_B=True)
    
    eig1 = np.sort(np.real(eigvals(P1)))
    eig2 = np.sort(np.real(eigvals(P2)))
    
    return np.allclose(eig1, eig2), eig1, eig2

def print_spectra(vals, decimals=2):
    """
    Pretty-print cospectrality check and spectra as row matrices.
    
    Parameters:
    -----------
    vals : tuple
        (ok, eig1, eig2) where ok is bool, eig1/eig2 are numpy arrays
    decimals : int
        Number of decimal places for formatting (default=2)
    """
    ok, eig1, eig2 = vals
    
    # Formatter for nice matrix-like display
    fmt = {'float_kind': lambda x: f"{x:6.{decimals}f}"}
    
    print("Cospectral?", ok)
    print("Spectrum 1:\n", np.array2string(eig1.reshape(1, -1), formatter=fmt))
    print("Spectrum 2:\n", np.array2string(eig2.reshape(1, -1), formatter=fmt))



# --- Example usage ---
G_L = nx.path_graph(3)
G_H = nx.cycle_graph(4)
cospec, eig1, eig2 = theorem_3_1(G_L, G_H)
print("Adjacency Cospectral:", cospec)    
cospec, eig1, eig2 = theorem_3_3(G_L, G_H)
print("Normalized Laplacian Cospectral:", cospec)
print("Eigenvalues 1:", eig1)
print("Eigenvalues 2:", eig2)
print("Are eigenvalues equal?", np.allclose(eig1, eig2))
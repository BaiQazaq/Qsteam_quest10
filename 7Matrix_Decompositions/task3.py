# Create a function to perform singular value decomposition.
# Создайте функцию для выполнения разложения по сингулярным значениям.

import numpy as np

def svd(matrix):
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix, dtype=float)
    m, n = matrix.shape

    # Perform SVD using NumPy's svd function
    U, s, Vt = np.linalg.svd(matrix, full_matrices=False)

    # Create the diagonal matrix Sigma
    Sigma = np.diag(s)

    return U, Sigma, Vt

# Example usage:
# Consider a matrix A
A = np.array([[4, -2, 1], [20, -7, 12], [-8, 13, 17]])

# Perform SVD
U, Sigma, Vt = svd(A)

print("Matrix A:")
print(A)

print("\nMatrix U:")
print(U)

print("\nDiagonal Matrix Sigma:")
print(Sigma)

print("\nMatrix Vt:")
print(Vt)

# Verify the decomposition by reconstructing the matrix A
A_reconstructed = U @ Sigma @ Vt
print("\nReconstructed Matrix (U * Sigma * Vt):")
print(A_reconstructed)

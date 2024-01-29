# Implement LU decomposition for a square matrix.
# Реализуйте LU-разложение для квадратной матрицы.

import numpy as np

def lu_decomposition(matrix):
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix, dtype=float)
    n = matrix.shape[0]

    # Initialize L and U matrices
    L = np.eye(n)
    U = np.zeros_like(matrix)

    # Perform LU decomposition (Doolittle algorithm)
    for k in range(n):
        U[k, k:] = matrix[k, k:] - L[k, :k] @ U[:k, k:]
        if k < n - 1:
            L[(k+1):, k] = (matrix[(k+1):, k] - L[(k+1):, :k] @ U[:k, k:]) / U[k, k]

    return L, U

# Example usage:
# Consider a square matrix A
A = np.array([[4, -2, 1], [20, -7, 12], [-8, 13, 17]])

# Perform LU decomposition
L, U = lu_decomposition(A)

print("Matrix A:")
print(A)

print("\nLower Triangular Matrix L:")
print(L)

print("\nUpper Triangular Matrix U:")
print(U)

# Verify the decomposition by multiplying L and U
A_reconstructed = L @ U
print("\nReconstructed Matrix (L * U):")
print(A_reconstructed)


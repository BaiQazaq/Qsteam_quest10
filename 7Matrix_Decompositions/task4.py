# Implement Cholesky decomposition for a symmetric positive-definite matrix.
# Реализуйте разложение Холецкого для симметричной положительно определенной матрицы.

import numpy as np

def cholesky_decomposition(matrix):
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix, dtype=float)
    
    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    # Check if the matrix is symmetric
    if not np.allclose(matrix, matrix.T):
        raise ValueError("Input matrix must be symmetric.")

    # Check if the matrix is positive-definite
    if not np.all(np.linalg.eigvals(matrix) > 0):
        raise ValueError("Input matrix must be positive-definite.")

    n = matrix.shape[0]
    L = np.zeros_like(matrix)

    for i in range(n):
        for j in range(i+1):
            if i == j:
                L[i, i] = np.sqrt(matrix[i, i] - np.sum(L[i, :]**2))
            else:
                L[i, j] = (matrix[i, j] - np.sum(L[i, :] * L[j, :])) / L[j, j]

    return L

# Example usage:
# Consider a symmetric positive-definite matrix A
A = np.array([[9, 3, -6], [3, 26, -7], [-6, -7, 9]])

# Perform Cholesky decomposition
L = cholesky_decomposition(A)

print("Matrix A:")
print(A)

print("\nLower Triangular Matrix L:")
print(L)

# Verify the decomposition by reconstructing the matrix A
A_reconstructed = L @ L.T
print("\nReconstructed Matrix (L * L^T):")
print(A_reconstructed)

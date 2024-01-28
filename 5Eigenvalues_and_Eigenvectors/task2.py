# Implement a method to compute the eigenvectors of a 2x2 matrix.
# Реализуйте метод для вычисления собственных векторов матрицы 2x2.

import numpy as np

def compute_eigenvectors(matrix):
    # Calculate the eigenvalues and eigenvectors using numpy's eig function
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvectors

# Example usage:
# Consider the 2x2 matrix: A = [[4, 2], [1, 3]]
matrix_A = np.array([[4, 2], [1, 3]])

# Find the eigenvectors
eigenvectors_A = compute_eigenvectors(matrix_A)

print("Eigenvectors of matrix A:")
for i, eigenvector in enumerate(eigenvectors_A.T):
    print(f"Eigenvalue {i+1}: {eigenvector}")

# Develop a program to find the null space of a matrix.
#Разработать программу для поиска нулевого пространства матрицы.

import numpy as np

def null_space(matrix):
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix, dtype=float)

    # Perform Singular Value Decomposition (SVD)
    _, _, Vt = np.linalg.svd(matrix, full_matrices=True)

    # Find the columns of Vt corresponding to zero singular values
    null_space_basis = Vt.T[:, np.isclose(_, 0.0)]

    return null_space_basis

# Example usage:
# Consider a matrix A
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Find the null space of matrix A
null_space_basis = null_space(A)

print("Matrix A:")
print(A)

print("\nNull Space Basis Vectors:")
print(null_space_basis)

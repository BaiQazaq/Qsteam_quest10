# Write a function to check if a matrix is diagonal.
# Напишите функцию, проверяющую, является ли матрица диагональной.

import numpy as np

def is_diagonal(matrix):
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix)

    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        return False

    # Check if all elements outside the main diagonal are zero
    return np.all(matrix * (1 - np.eye(matrix.shape[0])) == 0)

# Example usage:
# Consider a diagonal matrix: A = [[1, 0], [0, -2]]
diagonal_matrix = [[1, 0], [0, -2]]

# Check if the matrix is diagonal
result = is_diagonal(diagonal_matrix)

if result:
    print("The matrix is diagonal.")
else:
    print("The matrix is not diagonal.")

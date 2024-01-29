# Create a program to check if a matrix is symmetric.
# Создайте программу, проверяющую симметричность матрицы.
import numpy as np

def is_symmetric(matrix):
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix)

    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        return False

    # Check if the matrix is equal to its transpose
    return np.array_equal(matrix, matrix.T)

# Example usage:
# Consider a symmetric matrix: A = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
symmetric_matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]

# Check if the matrix is symmetric
result = is_symmetric(symmetric_matrix)

if result:
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")

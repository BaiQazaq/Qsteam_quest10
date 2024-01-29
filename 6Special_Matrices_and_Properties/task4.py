# Develop a program to identify if a matrix is a sparse matrix.
# Разработайте программу для определения того, является ли матрица разреженной.

import numpy as np

def is_sparse(matrix, threshold=0.8):
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix)

    # Calculate the percentage of non-zero elements
    non_zero_percentage = np.count_nonzero(matrix) / matrix.size

    # Check if the matrix is sparse based on the threshold
    return non_zero_percentage <= threshold

# Example usage:
# Consider a sparse matrix: A = [[1, 0, 0], [0, 0, 0], [0, 0, 3]]
sparse_matrix = [[1, 0, 0], [0, 0, 0], [0, 0, 3]]

# Check if the matrix is sparse
result = is_sparse(sparse_matrix)

if result:
    print("The matrix is sparse.")
else:
    print("The matrix is not sparse.")

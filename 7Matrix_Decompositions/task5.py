# Write a method to find the rank of a matrix using its decomposition.
# Напишите метод определения ранга матрицы с помощью ее разложения.

import numpy as np

def rank_using_svd(matrix):
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix, dtype=float)

    # Perform SVD using NumPy's svd function
    _, singular_values, _ = np.linalg.svd(matrix)

    # Set a tolerance for considering singular values as non-zero
    tolerance = max(matrix.shape) * np.spacing(np.max(singular_values))

    # Count the number of non-zero singular values
    rank = np.sum(singular_values > tolerance)

    return rank

# Example usage:
# Consider a matrix A
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate the rank using SVD
rank = rank_using_svd(A)

print("Matrix A:")
print(A)

print("\nRank of Matrix A:", rank)

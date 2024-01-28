# Write a program to find the eigenvalues of a 2x2 matrix.
# Напишите программу для поиска собственных значений матрицы 2x2.
import numpy as np

def find_eigenvalues(matrix):
    # Calculate the eigenvalues using numpy's eigvals function
    eigenvalues = np.linalg.eigvals(matrix)
    return eigenvalues

# Example usage:
# Consider the 2x2 matrix: A = [[4, 2], [1, 3]]
matrix_A = np.array([[4, 2], [1, 3]])

# Find the eigenvalues
eigenvalues_A = find_eigenvalues(matrix_A)

print("Eigenvalues of matrix A:", eigenvalues_A)

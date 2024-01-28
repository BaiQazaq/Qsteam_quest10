# Create a function to check if a given vector is an eigenvector of a matrix.
# Создайте функцию, проверяющую, является ли данный вектор собственным вектором матрицы.

import numpy as np

def is_eigenvector(matrix, eigenvalue, vector):
    # Calculate the left side of the equation Av
    left_side = np.dot(matrix, vector)
    
    # Calculate the right side of the equation λv
    right_side = eigenvalue * vector
    
    # Check if both sides are approximately equal
    return np.allclose(left_side, right_side)

# Example usage:
# Consider the matrix: A = [[4, 2], [1, 3]]
matrix_A = np.array([[4, 2], [1, 3]])

# Example eigenvector and eigenvalue
eigenvector_example = np.array([2, 1])
eigenvalue_example = 5

# Check if the eigenvector_example is an eigenvector for matrix_A with eigenvalue_example
result = is_eigenvector(matrix_A, eigenvalue_example, eigenvector_example)

if result:
    print("The vector is an eigenvector.")
else:
    print("The vector is not an eigenvector.")

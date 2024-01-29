# Implement a method to determine if a matrix is orthogonal.
# Реализуйте метод, чтобы определить, является ли матрица ортогональной
import numpy as np

def is_orthogonal(matrix):
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix)

    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        return False

    # Calculate the transpose of the matrix
    matrix_transpose = matrix.T

    # Calculate the inverse of the matrix
    try:
        matrix_inverse = np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        # The matrix is singular, and its inverse does not exist
        return False

    # Check if the transpose is equal to the inverse
    return np.array_equal(matrix_transpose, matrix_inverse)

# Example usage:
# Consider an orthogonal matrix: A = [[1, 0], [0, -1]]
orthogonal_matrix = [[1, 0], [0, -1]]

# Check if the matrix is orthogonal
result = is_orthogonal(orthogonal_matrix)

if result:
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")

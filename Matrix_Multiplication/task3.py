# Create a function to multiply a matrix by a vector.

def matrix_vector_multiply(matrix, vector):
    """
    Multiply a matrix by a vector.

    Parameters:
    - matrix (list of lists): The matrix to be multiplied.
    - vector (list): The vector to be multiplied.

    Returns:
    - list: The result of the multiplication.
    """

    # Check if the matrix and vector are compatible for multiplication
    if len(matrix[0]) != len(vector):
        raise ValueError("Incompatible dimensions for matrix-vector multiplication")

    # Perform matrix-vector multiplication
    result = [sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix]

    return result

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

vector = [2, 3, 4]

result = matrix_vector_multiply(matrix, vector)
print(result)

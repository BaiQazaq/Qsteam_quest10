#Implement a program for matrix-vector multiplication.
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

def main():
    # Example matrix and vector
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    vector = [2, 3, 4]

    try:
        # Perform matrix-vector multiplication
        result = matrix_vector_multiply(matrix, vector)

        # Display the result
        print("Matrix:")
        for row in matrix:
            print(row)

        print("\nVector:")
        print(vector)

        print("\nResult of Matrix-Vector Multiplication:")
        print(result)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

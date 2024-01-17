#Implement an element-wise multiplication of two matrices.

def elementwise_multiply(matrix1, matrix2):
    result = []

    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for element-wise multiplication.")
        return None

    # Iterate through each element and multiply corresponding elements
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix1[0])):
            row_result.append(matrix1[i][j] * matrix2[i][j])
        result.append(row_result)

    return result

# Example matrices
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Call the function to perform element-wise multiplication
result_matrix = elementwise_multiply(matrix_a, matrix_b)

# Print the result
if result_matrix:
    print("Matrix A:")
    for row in matrix_a:
        print(row)

    print("\nMatrix B:")
    for row in matrix_b:
        print(row)

    print("\nElement-wise Product of Matrices:")
    for row in result_matrix:
        print(row)

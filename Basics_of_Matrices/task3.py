#Create a function to perform scalar multiplication on a matrix

def scalar_multiply(matrix, scalar):
    result = []

    # Iterate through each element and multiply by the scalar
    for i in range(len(matrix)):
        row_result = []
        for j in range(len(matrix[0])):
            row_result.append(matrix[i][j] * scalar)
        result.append(row_result)

    return result

# Example matrix
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Scalar multiplier
scalar_value = 2

# Call the function to perform scalar multiplication
result_matrix = scalar_multiply(matrix_a, scalar_value)

# Print the result
print("Original Matrix:")
for row in matrix_a:
    print(row)

print("\nScalar Multiplied Matrix:")
for row in result_matrix:
    print(row)

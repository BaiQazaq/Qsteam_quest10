# Write a program to multiply two matrices

def multiply_matrices(matrix1, matrix2):
    result = []

    # Check if matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        print("Matrices cannot be multiplied. Invalid dimensions.")
        return None

    # Iterate through rows of the first matrix
    for i in range(len(matrix1)):
        row_result = []

        # Iterate through columns of the second matrix
        for j in range(len(matrix2[0])):
            # Calculate the dot product of the current row in matrix1 and current column in matrix2
            dot_product = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))

            row_result.append(dot_product)

        result.append(row_result)

    return result

# Example matrices
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Call the function to multiply matrices
result_matrix = multiply_matrices(matrix_a, matrix_b)

# Print the result
if result_matrix:
    print("Matrix A:")
    for row in matrix_a:
        print(row)

    print("\nMatrix B:")
    for row in matrix_b:
        print(row)

    print("\nProduct of Matrices:")
    for row in result_matrix:
        print(row)

                #NOTE: var2
        
# # Program to multiply two matrices using nested loops

# # 3x3 matrix
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# # 3x4 matrix
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]
# # result is 3x4
# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]

# # iterate through rows of X
# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]

# for r in result:
#    print(r)

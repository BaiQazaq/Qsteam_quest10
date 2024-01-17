# Write a program to add two matrices.

def add_matrices(matrix1, matrix2):
    result = []
    
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for addition.")
        return None
    
    # Iterate through each element and add corresponding elements
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix1[0])):
            row_result.append(matrix1[i][j] + matrix2[i][j])
        result.append(row_result)

    return result

    


# Example matrices
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Call the function to add matrices
result_matrix = add_matrices(matrix_a, matrix_b)

# Print the result
if result_matrix:
    print("Matrix A:")
    for row in matrix_a:
        print(row)

    print("\nMatrix B:")
    for row in matrix_b:
        print(row)

    print("\nSum of Matrices:")
    for row in result_matrix:
        print(row)

                            # NOTE: variant 2
# # Program to add two matrices using nested loop

# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]

# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]

# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]

# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#    for j in range(len(X[0])):
#        result[i][j] = X[i][j] + Y[i][j]

# for r in result:
#    print(r)

                            #NOTE: variant 3
        
# # Program to add two matrices using list comprehension
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]

# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]

# result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

# for r in result:
#    print(r)
#Write a method to transpose a matrix.

# Program to transpose a matrix using a nested loop

initial_mtrx = [[12,7],
    [4 ,5],
    [3 ,8]]

transposed = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(initial_mtrx)):
   # iterate through columns
   for j in range(len(initial_mtrx[0])):
       transposed[j][i] = initial_mtrx[i][j]

for r in transposed:
   print(r)


                    #NOTE: variant2
   
# ''' Program to transpose a matrix using list comprehension'''
# X = [[12,7],
#     [4 ,5],
#     [3 ,8]]

# result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

# for r in result:
#    print(r)

                        #NOTE: variant3
# def transpose_matrix(matrix):
#     # Use zip to transpose rows and columns
#     transposed_matrix = list(map(list, zip(*matrix)))

#     return transposed_matrix

# # Example matrix
# matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # Call the function to transpose the matrix
# transposed_matrix = transpose_matrix(matrix_a)

# # Print the result
# print("Original Matrix:")
# for row in matrix_a:
#     print(row)

# print("\nTransposed Matrix:")
# for row in transposed_matrix:
#     print(row)

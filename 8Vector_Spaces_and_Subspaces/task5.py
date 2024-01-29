# Write a function to calculate the dimension of a vector space.
# Напишите функцию для вычисления размерности векторного пространства.

import numpy as np

def vector_space_dimension(vectors):
    # Convert the vectors to a NumPy array
    matrix = np.array(vectors, dtype=float).T

    # Perform row reduction using Gaussian elimination
    reduced_matrix, pivot_columns = row_reduction(matrix)

    # Count the number of pivot columns, which is the dimension of the vector space
    dimension = len(pivot_columns)

    return dimension

def row_reduction(matrix):
    # Perform row reduction (Gaussian elimination)
    row, col = 0, 0
    num_rows, num_cols = matrix.shape

    pivot_columns = []

    while row < num_rows and col < num_cols:
        # Find pivot for this column
        pivot_row = np.argmax(np.abs(matrix[row:, col])) + row
        if matrix[pivot_row, col] != 0:
            # Add the column index to the list of pivot columns
            pivot_columns.append(col)

            # Swap rows
            matrix[[row, pivot_row]] = matrix[[pivot_row, row]]

            # Normalize the pivot row
            matrix[row] /= matrix[row, col]

            # Eliminate other rows
            for i in range(num_rows):
                if i != row:
                    matrix[i] -= matrix[i, col] * matrix[row]

            row += 1

        col += 1

    return matrix, pivot_columns

# Example usage:
# Consider a set of vectors
vectors = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# Calculate the dimension of the vector space
dimension = vector_space_dimension(vectors)

print("Set of Vectors:")
print(np.array(vectors))

print("\nDimension of the Vector Space:", dimension)

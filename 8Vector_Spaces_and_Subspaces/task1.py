# Write a program to check if a set of vectors spans a vector space.
# Напишите программу, проверяющую, охватывает ли набор векторов векторное пространство.

import numpy as np

def spans_vector_space(vectors):
    # Convert the vectors to a NumPy array
    matrix = np.array(vectors, dtype=float).T

    # Perform row reduction using Gaussian elimination
    reduced_matrix, _ = row_reduction(matrix)

    # Check if every row has a pivot position
    return all(np.any(reduced_matrix[i] != 0) for i in range(reduced_matrix.shape[0]))

def row_reduction(matrix):
    # Perform row reduction (Gaussian elimination)
    row, col = 0, 0
    num_rows, num_cols = matrix.shape

    while row < num_rows and col < num_cols:
        # Find pivot for this column
        pivot_row = np.argmax(np.abs(matrix[row:, col])) + row
        if matrix[pivot_row, col] != 0:
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

    return matrix, row

# Example usage:
# Consider a set of vectors
vectors = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Check if the set of vectors spans the vector space
spans_space = spans_vector_space(vectors)

print("Set of Vectors:")
print(np.array(vectors))

if spans_space:
    print("\nThe set of vectors spans the vector space.")
else:
    print("\nThe set of vectors does not span the vector space.")

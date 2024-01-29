# Implement a method to find the basis of a vector space.
# Реализуйте метод поиска основы векторного пространства.

import numpy as np

def find_basis(vectors):
    # Convert the vectors to a NumPy array
    matrix = np.array(vectors, dtype=float).T

    # Perform row reduction using Gaussian elimination
    reduced_matrix, pivot_columns = row_reduction(matrix)

    # Extract the linearly independent vectors from the original set
    basis_vectors = np.array([vectors[i] for i in pivot_columns])

    return basis_vectors

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

# Find the basis of the vector space
basis = find_basis(vectors)

print("Set of Vectors:")
print(np.array(vectors))

print("\nBasis of the Vector Space:")
print(basis)

# Create a function to check if a vector is in the column space of a matrix.
# Создайте функцию, чтобы проверить, находится ли вектор в пространстве столбцов матрицы.

import numpy as np

def is_in_column_space(matrix, vector):
    # Convert the matrix and vector to NumPy arrays
    matrix = np.array(matrix, dtype=float)
    vector = np.array(vector, dtype=float)

    # Augment the matrix with the vector
    augmented_matrix = np.column_stack((matrix, vector))

    # Perform row reduction using Gaussian elimination
    reduced_matrix, pivot_columns = row_reduction(augmented_matrix)

    # Check if the last column is a pivot column
    return reduced_matrix.shape[1] - 1 in pivot_columns

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
# Consider a matrix A and a vector b
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([4, 5, 6])

# Check if the vector b is in the column space of matrix A
result = is_in_column_space(A, b)

print("Matrix A:")
print(A)

print("\nVector b:")
print(b)

if result:
    print("\nThe vector b is in the column space of matrix A.")
else:
    print("\nThe vector b is not in the column space of matrix A.")

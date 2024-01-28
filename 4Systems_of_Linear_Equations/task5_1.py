# Implement the Gaussian elimination method to solve a system of linear equations.

import numpy as np

def gaussian_elimination(A, B):
    # Combine the coefficient matrix A and the constants B into an augmented matrix
    augmented_matrix = np.column_stack((A, B))

    # Perform Gaussian elimination to convert the augmented matrix to row-echelon form
    rows, cols = augmented_matrix.shape
    for i in range(min(rows, cols - 1)):
        # Make the diagonal element 1
        pivot = augmented_matrix[i, i]
        augmented_matrix[i, :] /= pivot

        # Eliminate other elements in the current column
        for j in range(i + 1, rows):
            factor = augmented_matrix[j, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

    # Back-substitution to find the solution
    solution = np.zeros(cols - 1)
    for i in range(rows - 1, -1, -1):
        solution[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:-1], solution[i+1:])

    return solution

# Example usage:
# Consider the system of equations: 2x + y = 5, 4x + 2y = 10
A = np.array([[2, 1], [4, 2]])
B = np.array([5, 10])

solution = gaussian_elimination(A, B)
print("Solution:", solution)



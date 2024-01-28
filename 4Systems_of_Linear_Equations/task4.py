# Write a function to check if a system of equations has no solution, one solution, or infinitely many solutions.

import numpy as np

def check_system(A, B):
    # Check if matrix A is invertible
    det_A = np.linalg.det(A)
    rank_A = np.linalg.matrix_rank(A)
    augmented_matrix_rank = np.linalg.matrix_rank(np.column_stack((A, B)))

    if det_A != 0:
        if rank_A == augmented_matrix_rank:
            return "The system has a unique solution."
        else:
            return "The system has infinitely many solutions."
    else:
        if rank_A == augmented_matrix_rank:
            return "The system has no solutions."
        else:
            return "The system has infinitely many solutions."

# Example usage:
# Consider the system of equations: 2x + y = 5, 4x + 2y = 10
A = np.array([[2, 1], [4, 2]])
B = np.array([5, 10])

result = check_system(A, B)
print(result)

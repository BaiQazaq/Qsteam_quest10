# Create a program to use matrix inversion to solve a system of equations.

import numpy as np

def solve_linear_system(A, B):
    # Check if the matrix A is invertible
    if np.linalg.det(A) == 0:
        print("Matrix A is singular. The system may have no unique solution.")
        return None

    # Calculate the inverse of matrix A
    A_inv = np.linalg.inv(A)

    # Solve for vector x using the formula x = A_inv * B
    x = np.dot(A_inv, B)

    return x

# Example usage:
# Consider the system of equations: 2x + y = 5, 3x - 2y = 1
A = np.array([[2, 1], [3, -2]])
B = np.array([5, 1])

solution = solve_linear_system(A, B)

if solution is not None:
    print("Solution:", solution)
else:
    print("No unique solution.")

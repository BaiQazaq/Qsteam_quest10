# Write a program to create an identity matrix of size n.
# Напишите программу для создания единичной матрицы размера n

import numpy as np

def create_identity_matrix(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n should be a positive integer.")

    # Create the identity matrix using NumPy
    identity_matrix = np.eye(n)

    return identity_matrix

# Example usage:
# Create a 3x3 identity matrix
n = 3
identity_matrix_3x3 = create_identity_matrix(n)

print(f"Identity matrix of size {n}x{n}:\n{identity_matrix_3x3}")

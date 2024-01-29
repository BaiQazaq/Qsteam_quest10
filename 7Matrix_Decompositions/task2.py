# Write a program for QR decomposition of a matrix.
# Напишите программу QR-разложения матрицы.

import numpy as np

def qr_decomposition(matrix):
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix, dtype=float)
    m, n = matrix.shape

    # Initialize Q and R matrices
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    # Gram-Schmidt process for QR decomposition
    for j in range(n):
        v = matrix[:, j]
        for i in range(j):
            R[i, j] = Q[:, i] @ matrix[:, j]
            v -= R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    return Q, R

# Example usage:
# Consider a matrix A
A = np.array([[4, -2, 1], [20, -7, 12], [-8, 13, 17]])

# Perform QR decomposition
Q, R = qr_decomposition(A)

print("Matrix A:")
print(A)

print("\nOrthogonal Matrix Q:")
print(Q)

print("\nUpper Triangular Matrix R:")
print(R)

# Verify the decomposition by multiplying Q and R
A_reconstructed = Q @ R
print("\nReconstructed Matrix (Q * R):")
print(A_reconstructed)

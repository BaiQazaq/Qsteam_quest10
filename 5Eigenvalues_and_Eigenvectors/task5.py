# Implement a procedure to demonstrate the power method for finding dominant eigenvalues.
# Реализуйте процедуру, чтобы продемонстрировать степенной метод для поиска доминирующих собственных значений

import numpy as np

def power_iteration(matrix, num_iterations=100):
    # Choose a random initial vector
    v = np.random.rand(matrix.shape[0])

    for _ in range(num_iterations):
        # Apply the matrix to the vector
        Av = np.dot(matrix, v)

        # Find the dominant eigenvalue
        eigenvalue = np.linalg.norm(Av, ord=np.inf)

        # Normalize the vector
        v = Av / eigenvalue

    return eigenvalue, v

# Example usage:
# Consider the matrix: A = [[4, 2], [1, 3]]
matrix_A = np.array([[4, 2], [1, 3]])

# Find the dominant eigenvalue and eigenvector using power iteration
dominant_eigenvalue, dominant_eigenvector = power_iteration(matrix_A)

print("Dominant Eigenvalue:", dominant_eigenvalue)
print("Dominant Eigenvector:", dominant_eigenvector)

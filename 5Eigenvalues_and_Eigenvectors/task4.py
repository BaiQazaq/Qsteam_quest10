# Develop a program to find the characteristic polynomial of a matrix.
# Разработать программу для нахождения характеристического полинома матрицы.

import numpy as np
from sympy import Matrix, symbols

def characteristic_polynomial(matrix):
    # Создаем символьную переменную lambda
    lambda_symbol = symbols('lambda')

    # Преобразуем матрицу в символьную матрицу
    symbolic_matrix = Matrix(matrix)

    # Вычисляем характеристический полином
    char_poly = symbolic_matrix.charpoly(lambda_symbol)

    return char_poly

# Пример использования:
# Рассмотрим матрицу: A = [[4, 2], [1, 3]]
matrix_A = np.array([[4, 2], [1, 3]])

# Найдем характеристический полином
char_poly_A = characteristic_polynomial(matrix_A)

# Выведем характеристический полином
print("Характеристический полином матрицы A:")
print(char_poly_A)

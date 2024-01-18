# Implement a program to verify if a matrix is invertible.
# Реализуйте программу, проверяющую, является ли матрица обратимой
from task1 import determinant_2_2
from task2 import determinant_3x3



def check_inverse(mtrx):
    if len(mtrx) == 2:
        res = determinant_2_2(mtrx)
        if res:
            print(f"Matrix is invertible")
        else:
            print(f"Matrix is NOT invertible")
    elif len(mtrx) == 3:
        res = determinant_3x3(mtrx)
        if res:
            print(f"Matrix is invertible")
        else:
            print(f"Matrix is NOT invertible")

matrix_1 = [
    [0, 1],
    [0, 1]
]
matrix_2 = [
    [1, 1],
    [0, 1]
]
matrix_3 = [
    [0, 1, 3],
    [0, 1, 2],
    [2, 3, 5]
]

check_inverse(matrix_1)
check_inverse(matrix_2)
check_inverse(matrix_3)
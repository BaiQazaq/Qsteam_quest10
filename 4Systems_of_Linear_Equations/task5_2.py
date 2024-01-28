# Implement the Gaussian elimination method to solve a system of linear equations.

# Смысл метода: последовательно исключаем переменную за переменной, 
# пока в одной из строк не будет однозначно определена переменная xi. 
# Идею можно проиллюстрировать на простом примере:
#  x1 - x2 = 3
# -x1 + 2x2 = 1
# =========== (складываем строки)
#       -x2 + 2x2= 3 + 1 = 4 или x2 = 4
# Откуда, x1 = 7

# ПРИМЕР.
# 2x1-x2=0
# -x1+x2+4x3=13
# x1+2x2+3x3=14

# Решение.
# Запишем систему в виде расширенной матрицы:
matrix_initial = [
    [2, -1, 0, 0],
    [-1, 1, 4, 13],
    [1, 2, 3, 14]
]
# Далее умножаем 2-ую строку на (2) и добавляем к первой:

for i in range(1):
    for j in range(4):
        matrix_initial[i][j] = matrix_initial[i][j] + matrix_initial[i+1][j] * 2


#Добавим 3-ую строку к 2-ой:
for i in range(1):
    for j in range(4):
        matrix_initial[i+1][j] = matrix_initial[i+1][j] + matrix_initial[i+2][j]
print(matrix_initial)

#Умножим первую строчку на (3), 2-ую строку умножаем на (-1). 
#Следующее действие: складываем первую и вторую строки:
for i in range(1):
    for j in range(4):
        matrix_initial[i][j] = (matrix_initial[i][j] * 3) + (matrix_initial[i+1][j] * -1)
# В результате получится следующая матрица
#   0	0	17 51
#   0	3	7  27
#   1	2	3  14
    
# Теперь исходную систему можно записать как:
    
# x3 = 51/17 = 3
# x2 = [27 - 7x3]/3 = 2
# x1 = [14 - (2x2 + 3x3)] = 1

row = []
cnt = 0
for i in matrix_initial:
    if cnt == 0:
        res = (matrix_initial[0][3] - matrix_initial[0][0] - matrix_initial[0][1]) / matrix_initial[0][2]
        row.append(res)
        cnt += 1
    elif cnt == 1:
        res = (matrix_initial[1][3] - matrix_initial[1][0] - matrix_initial[1][2]*row[0]) / matrix_initial[1][1]
        row.append(res)
        cnt += 1
    elif cnt == 2:
        res = (matrix_initial[2][3] - (matrix_initial[2][1]*row[1] + matrix_initial[2][2]*row[0])) / matrix_initial[2][0]
        row.append(res)
        cnt += 1
print(f"X3 = {int(row[0])} \nX2 = {int(row[1])} \nX1 = {int(row[2])}")
    

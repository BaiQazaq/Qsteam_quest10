# Create a function to compute the inverse of a 2x2 matrix.
from task1 import determinant_2_2

def adjoint_mtrx(mtrx):     #транспонированние матрицы
    new_mtrx = []
    row1 = [mtrx[1][1], mtrx[0][1] * -1]
    row2 = [mtrx[1][0]* -1, mtrx[0][0]]
    new_mtrx.append(row1)
    new_mtrx.append(row2)
    return new_mtrx

def inverse_mtrx(mtrx):
    inversed = []
    res_det = determinant_2_2(mtrx)
    print(f"det = {res_det}")
    if res_det == 0:
        print(f"Matrix with determinat = 0")
    
    adj_mtrx = adjoint_mtrx(mtrx)
    print(f"Adjointed = {adj_mtrx}")
    for i in range(2):
        row_result = []
        for j in range(2):
            row_result.append((1/res_det) * adj_mtrx[i][j])
        inversed.append(row_result)

    return inversed

matrix =[
    [1, -1],
    [0, 2]
]



if __name__ == "__main__":
    result = inverse_mtrx(matrix)

    if result:
        print(f"Inversed matrix 2x2 = {result}")
# Write a method to find the inverse of a 3x3 matrix
from task2 import determinant_3x3

def adjoint_mtrx(mtrx):
    new_mtrx = []
    row1 = [mtrx[0][0], mtrx[0][1], mtrx[2][0]]
    row2 = [mtrx[1][0], mtrx[1][1], mtrx[2][1]]
    row3 = [mtrx[0][2], mtrx[1][2], mtrx[2][2]]
    new_mtrx.append(row1)
    new_mtrx.append(row2)
    new_mtrx.append(row3)
    return new_mtrx

def algebraic_complement(mtrx):
    row1 = []
    row2 = []
    row3 = []
    res_alg = []
    for i in range(9):
        i += 1
        match i:
                case 1:
                    el_1_1 = (mtrx[1][1]*mtrx[2][2] - mtrx[1][2]*mtrx[2][1]) * ((-1)** (1+1))
                    row1.append(el_1_1)
                case 2:
                    el_1_2 = (mtrx[1][0]*mtrx[2][2] - mtrx[1][2]*mtrx[2][0]) * ((-1)** (1+2))
                    row1.append(el_1_2)
                case 3:
                    el_1_3 = (mtrx[1][0]*mtrx[2][1] - mtrx[1][1]*mtrx[2][0]) * ((-1)** (1+3))
                    row1.append(el_1_3)
                case 4:
                    el_2_1 = (mtrx[0][1]*mtrx[2][2] - mtrx[0][2]*mtrx[2][1]) * ((-1)** (2+1))
                    row2.append(el_2_1)
                case 5:
                    el_2_2 = (mtrx[0][0]*mtrx[2][2] - mtrx[0][2]*mtrx[2][0]) * ((-1)** (2+2))
                    row2.append(el_2_2)
                case 6:
                    el_2_3 = (mtrx[0][0]*mtrx[2][1] - mtrx[0][1]*mtrx[2][0]) * ((-1)** (2+3))
                    row2.append(el_2_3)
                case 7:
                    el_3_1 = (mtrx[0][1]*mtrx[1][2] - mtrx[0][2]*mtrx[1][1]) * ((-1)** (3+1))
                    row3.append(el_3_1)
                case 8:
                    el_3_2 = (mtrx[0][0]*mtrx[1][2] - mtrx[0][2]*mtrx[1][0]) * ((-1)** (3+2))
                    row3.append(el_3_2)
                case 9:
                    el_3_3 = (mtrx[0][0]*mtrx[1][1] - mtrx[0][1]*mtrx[1][0]) * ((-1)** (3+3))
                    row3.append(el_3_3)
                case _:
                    print('!!!  Wrong command !!!')
    res_alg.append(row1)
    res_alg.append(row2)
    res_alg.append(row3)
    return res_alg
    
    

def inverse_mtrx(mtrx):
    inversed = []
    res_det = determinant_3x3(mtrx)
    print(f"det = {res_det}")
    if res_det == 0:
        print(f"Matrix with determinat = 0")
    
    adj_mtrx = adjoint_mtrx(mtrx)
    print(f"Adjointed = {adj_mtrx}")
    result_alg_compl = algebraic_complement(adj_mtrx)
    for i in range(3):
        row_result = []
        for j in range(3):
            row_result.append((1/res_det) * result_alg_compl[i][j])
        inversed.append(row_result)
    return inversed

matrix = [
    [-1, 2, -2],
    [2, -1, 5],
    [3, -2, 4]
]

result = inverse_mtrx(matrix)

if result:
    print(f"Inversed matrix 3x3 = {result}")


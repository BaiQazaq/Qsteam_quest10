# Solve a system of two linear equations using matrices.

def determinant_2_2(mtrx):
    if len(mtrx[0]) != 2 or len(mtrx[1]) != 2 or len(mtrx) != 2:
        print("Matrix should be 2 x 2")
        return 0
    
    scalar = mtrx[0][0] * mtrx[1][1] - mtrx[0][1] * mtrx[1][0]
    return scalar

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


def liner_eq_by_mtrx(A_mtrx, X_mtrx, B_mtrx):
    inversed = inverse_mtrx(A_mtrx)    
    for i in range(len(inversed)):
        new_el = 0
        for j in range(len(inversed)):
            
            new_el += (inversed[i][j] * B_mtrx[j])
        X_mtrx[i] = new_el
    return X_mtrx


ln1 = 3
ln2 = 2
rn1 = 5/6
rn2 = 2
x1 = 'x1'
x2 = 'x2'
liner_equation1 = "3 * x1 - 2 * x2 = 5/6"
liner_equation2 = "2 * x1 + 3 * x2 = 2"
A_mtrx = [
    [3, -2],
    [2, 3]
]
X_mtrx = [
    [x1],
    [x2]
]
B_mtrx = [5/6, 2]

if __name__ == "__main__":
    result = liner_eq_by_mtrx(A_mtrx, X_mtrx, B_mtrx)

    print(f"X1 = {result[0]}, X2 = {result[1]}")
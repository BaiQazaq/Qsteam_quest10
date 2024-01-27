# Implement a method to solve a system of three linear equations.

def vector_build(lst_all):
    vector = []
    for i in range(len(lst_all)):
        for j in range(len(lst_all[i])-2):
            if lst_all[i][j] == '=':
                if lst_all[i][j+1] == '-':
                    vector.append(int(lst_all[i][j+2])*-1)
                else:
                    vector.append(int(lst_all[i][j+2]))   
    print(f"vector = {vector}")
    return vector

def exctract_x_val(lst_all):
    mtrx = []
    for i in range(len(lst_all)):
        row = []
        for j in range(len(lst_all[i])-2):
            if lst_all[i][j] == 'x':
                if (j-1) != -1 and lst_all[i][j-1].isdigit():
                    if lst_all[i][j-2] == '-':
                        row.append([int(lst_all[i][j-1]) * -1, int(lst_all[i][j+1])])
                    else:
                        row.append([int(lst_all[i][j-1]), int(lst_all[i][j+1])])
                else:
                    if lst_all[i][j-2] == '-':
                        row.append([-1, int(lst_all[i][j+1])])
                    else:
                        row.append([1, int(lst_all[i][j+1])])
        mtrx.append(row)
    print(mtrx)
    return mtrx

def build_initial_mtrx(mtrx):
    row_matrix = exctract_x_val(mtrx)
    matrix = []
    for i in range(len(row_matrix)):
        row = [0, 0, 0]
        for j in range(len(row_matrix[i])):
            if row_matrix[i][j][1] == 1:
                row.pop(0)
                row.insert(0, row_matrix[i][j][0])
            elif row_matrix[i][j][1] == 2:
                row.pop(1)
                row.insert(1, row_matrix[i][j][0])
            elif row_matrix[i][j][1] == 3:
                row.pop(2)
                row.insert(2, row_matrix[i][j][0])
        matrix.append(row)
    return matrix



def determinant_3x3(mtrx):
    if len(mtrx[0]) != 3 or len(mtrx[1]) != 3 or len(mtrx) != 3:
        print("Matrix should be 3 x 3")
        return 0
    mark_mtrx = """
        [+ - +]
        [- + -]
        [+ - +]
    """
    
    num1 = mtrx[0][0]*(mtrx[1][1]*mtrx[2][2] - mtrx[1][2]*mtrx[2][1])
    num2 = mtrx[0][1]*(mtrx[1][0]*mtrx[2][2] - mtrx[1][2]*mtrx[2][0])
    num3 = mtrx[0][2]*(mtrx[1][0]*mtrx[2][1] - mtrx[1][1]*mtrx[2][0])
    scalar = num1 - num2 + num3
    return scalar

def adjoint_mtrx(mtrx):  
    new_mtrx = []
    row1 = [mtrx[0][0], mtrx[0][1], mtrx[2][0]]
    row2 = [mtrx[1][0], mtrx[1][1], mtrx[2][1]]
    row3 = [mtrx[0][2], mtrx[1][2], mtrx[2][2]]
    new_mtrx.append(row1)
    new_mtrx.append(row2)
    new_mtrx.append(row3)
    return new_mtrx

def algebraic_complement(mtrx):   #Алгебраические дополнения.
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
    matrix = build_initial_mtrx(mtrx)
    print(matrix)
    inversed = []
    res_det = determinant_3x3(matrix)
    print(f"det = {res_det}")
    if res_det == 0:
        print(f"Matrix with determinat = 0")
    
    adj_mtrx = adjoint_mtrx(matrix)
    print(f"Adjointed = {adj_mtrx}")
    result_alg_compl = algebraic_complement(adj_mtrx)
    for i in range(3):
        row_result = []
        for j in range(3):
            row_result.append((1/res_det) * result_alg_compl[i][j])
        inversed.append(row_result)
    return inversed

def solve_stlq(lst_all):
    inversed_mtrx = inverse_mtrx(lst_all)
    vector = vector_build(lst_all)
    result_stlq = []
    for i in range(len(inversed_mtrx)):
        result_stlq.append(inversed_mtrx[i][0] * vector[0] + inversed_mtrx[i][1] * vector[1] + inversed_mtrx[i][2] * vector[2])
    return result_stlq



line_1 = 'x1 + x3 = 4'
line_2 = '2x2 - x3 = 1'
line_3 = '3x1 - x2 = 1'
lst1 = list(line_1)
lst2 = list(line_2)
lst3 = list(line_3)
lst_all = [lst1, lst2, lst3]

result = solve_stlq(lst_all)
print(result)
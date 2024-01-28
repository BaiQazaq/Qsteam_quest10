# Implement a program to find the determinant of a 3x3 matrix

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

matrix = [
    [1, -2, 3],
    [4, 0, 6],
    [-7, 8, 9]
]

if __name__ == "__main__":
    result = determinant_3x3(matrix)

    if result:
        print(f"Determinat of the matrix {matrix}\nscalar values = {result}")
#Write a function to calculate the determinant of a 2x2 matrix

def determinant_2_2(mtrx):
    if len(mtrx[0]) != 2 or len(mtrx[1]) != 2 or len(mtrx) != 2:
        print("Matrix should be 2 x 2")
        return 0
    
    scalar = mtrx[0][0] * mtrx[1][1] - mtrx[0][1] * mtrx[1][0]
    return scalar

matrix = [
    [2, 5, 2],
    [6, 8]
]

if __name__ == "__main__":
    result = determinant_2_2(matrix)

    if result:
        print(f"Determinat of the matrix {matrix}\nscalar values = {result}")
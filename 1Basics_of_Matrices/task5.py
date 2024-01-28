#Implement a program to check if two matrices are equal.

def check_equality(mtrx1, mtrx2):
    if len(mtrx1) == len(mtrx2):
        for i in range(len(mtrx1)):
            if len(mtrx1[i]) != len(mtrx2[i]):
                print(f"The {i} elements of matrices have not the same dimensions.")
                return None
    else:
        print("Matrices must have the same dimensions.")
        return None

    for i in range(len(mtrx1)):
        for j in range(len(mtrx1[i])):
            if mtrx1[i][j] != mtrx2[i][j]:
                return 0
    return 1

matrix_A= [ [1, 1, 1, 1], 
            [2, 2, 2, 2], 
            [3, 3, 3, 3], 
            [4, 4, 4, 4]
            ] 
   
matrix_B= [ [1, 1, 1, 1], 
            [2, 2, 2, 2], 
            [3, 3, 3, 3], 
            [4, 4, 4, 4]
            ] 

result = check_equality(matrix_A, matrix_B)

if result:
    print("Matrices are identical") 
else: 
    print("Matrices are not identical") 
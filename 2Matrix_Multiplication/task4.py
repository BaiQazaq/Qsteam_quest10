#Develop a method to calculate the dot product of two vectors.

def dot_product(vctr1, vctr2):
    new_vctr = []
    if len(vctr1) != len(vctr2):
        print("Vectors must have the same dimensions for dot product.")
        return None
    
    for i in range(len(vctr1)):
        new_vctr.append(vctr1[i]*vctr2[i])
    
    return new_vctr

vector1 = [9, 8, 7]
vector2 = [6, 5, 4]

result = dot_product(vector1, vector2)

if result:
    print(f"Vector 1 = {vector1}\nVector 2 = {vector2}\nResult = {result}")
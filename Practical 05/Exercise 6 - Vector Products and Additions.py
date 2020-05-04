##scalar = 2.5
##vector = [1,2,3]

##def scalar_product(scalar, vector):
##    new_vector = []
##
##    for i in range(len(vector)):
##        scalar_product = vector[i] * scalar
##        new_vector.append(scalar_product)
##    print(new_vector)
##
##scalar_product(scalar, vector)


vector1 = [1,2,3]
vector2 = [9,8,7]

def vector_addition(vector1, vector2):
    new_vector = []

    for i in range(len(vector1)):
        vector_addition = vector1[i] + vector2[i]
        new_vector.append(vector_addition)
    print(new_vector)

vector_addition(vector1, vector2)
    

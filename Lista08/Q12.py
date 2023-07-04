import random
mat=[0]*56
matT=[0]*7
for i in range (7):
    matT[i]=[0]*56
for i in range (56):
    mat[i]=[0]*7
    for j in range (7):
        mat[i][j]=random.randint(1,9)
        matT[j][i]=mat[i][j]
    print (mat[i])
for i in range (7):
    print (matT[i])
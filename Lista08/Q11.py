import random
mat=[0]*5
soma=0
cont=4
for i in range (5):
    mat[i]=[0]*5
    for j in range (5):
        mat[i][j]=random.randint(1,10)
    soma+=mat[i][cont]
    cont-=1
    print (mat[i])
print (soma)
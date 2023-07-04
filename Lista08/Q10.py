import random
mat=[0]*22
soma=0
for i in range (22):
    mat[i]=[0]*22
    for j in range (22):
        mat[i][j]=random.randint(1,10)
    soma+=mat[i][i]
    print (mat[i])
print(soma)
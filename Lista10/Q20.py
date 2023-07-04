def matmais10(x):
    cont=0
    for i in range (4):
        for j in range(4):
            if mat[i][j]>10:
                cont+=1
    return cont
import random
mat=[0]*4
for i in range(4):
    mat[i]=[0]*4
    for j in range(4):
        mat[i][j]=random.randint(1,25)
    print (mat[i])
print (f'Essa matriz tem {matmais10(mat)} números maiores que 10.')
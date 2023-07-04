import random
mat=[0]*18
soma=0
cont=0
for i in range (18):
    mat[i]=[0]*18
    for j in range (18):
        mat[i][j]=random.randint(1,10)
        if i>0 and j<cont:
            soma=soma+mat[i][j]
    cont+=1
    print(mat[i])
print(soma)
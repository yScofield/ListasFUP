import random
mat=[0]*17
vetor=[]
soma=0
for i in range (17):
    mat[i]=[0]*17
    for j in range (17):
        mat[i][j]=random.randint(1,9)
    print(mat[i])
for i in range (17):
    for j in range (17):
        soma+=mat[j][i]
    vetor.append(soma)
    soma=0
print ('')
print (vetor)
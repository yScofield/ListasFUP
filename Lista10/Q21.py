def matid(x):
    dp=13*1
    resto=13*12
    for i in range(13):
        for j in range(13):
            if i==j and mat[i][j]==1:
                dp-=1
            if i!=j and mat[i][j]==0:
                resto-=1

    if dp==0 and resto==0:
        print ('É uma matriz identidade.')
    else:
        print ('Não é matriz identidade.')

import random
mat=[0]*13
for i in range(13):
    mat[i]=[0]*13
    for j in range(13):
            #mat[i][j]=random.randint(0,1)
            #mat[i][j]=int(input(f'Digite um valor em linha({i+1}) e coluna({j+1}): '))]
            if i==j:
                mat[i][j]=1
    print (mat[i])
matid(mat)
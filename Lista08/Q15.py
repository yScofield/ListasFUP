import random
A=[0]*5
B=[0]*5
C=[0]*5

for i in range (5):
    A[i]=[0]*5
    B[i]=[0]*5
    C[i]=[0]*5
    for j in range (5):
        A[i][j]=random.randint(1,5)
        B[i][j]=random.randint(1,5)
        for k in range (5):
            C[i][j]+=A[i][k]*B[i][k]
        
    print(f'{A[i]}   {B[i]}   {C[i]}')
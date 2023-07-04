import random
A=[0]*17
B=[0]*17
C=[0]*17
for i in range(17):
    A[i]=[0]*10
    B[i]=[0]*10
    C[i]=[0]*10
    for j in range(10):
        A[i][j]=random.randint(11,20)
        B[i][j]=random.randint(11,20)
        C[i][j]=A[i][j]+B[i][j]
    print(f'{A[i]}   {B[i]}   {C[i]}')
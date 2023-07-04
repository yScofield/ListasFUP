import random
A=[0]*10
B=[0]*10
C=[0]*10
for i in range (10):
    A[i]= random.randint(1,20)
    B[i]= random.randint(1,20)
    C[i]= A[i]-B[i]
print (f'{A}\n{B}\n{C}')
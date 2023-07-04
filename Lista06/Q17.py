import random
A=[0]*10
B=[0]*10
C=[0]*20
CP=0
CI=0
for i in range(10):
    A[i]=random.randint(1,10)
    B[i]=random.randint(1,10)
for i in range (20):
    if i%2==0:
        C[i]=A[CP]
        CP+=1
    else:
        C[i]=B[CI]
        CI+=1
print (A)
print (B)
print (C)
import random
A=[0]*20
cont=0
for i in range (20):
    A[i]=random.randint(1,20)
print (A)
for i in range (20):
    for j in range(20):
        if i!=j:
            if A[i]==A[j]:
                cont+=1
    if cont==0:
        print (f'{A[i]:4}', end="")
    cont=0
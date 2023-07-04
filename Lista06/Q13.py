import random
A=[0]*10
cont=0
for i in range (10):
    A[i]=random.randint(1,10)
print (A)
for i in range (10):
    for j in range (10):
        if i!=j:
            if A[i]==A[j]:
                cont+=1
                A[j]=' '
    if cont!=0 and A[i]!=' ':
        print (f'O {A[i]} se repete.')
    cont=0
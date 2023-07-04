import random
A=[0]*10
for i in range (10):
    A[i]= random.randint(1,50)
print (A)
x= int(input('Digite um número: '))
for i in range (10):
    if A[i]%x==0:
        print (A[i])
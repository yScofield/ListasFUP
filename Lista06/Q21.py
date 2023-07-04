import random
A= [0]*10
for i in range (10):
    A[i]=int(input('Digite um valor: '))
    c=1
    div=0
    while c<=A[i]:
        if A[i]%c==0:
            div+=1
        c+=1
    if div == 2:
        print (f'Número: {A[i]} Posição: {i}')
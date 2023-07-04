import random
A= [0]*100
for i in range (100):
    A[i]=random.randint(1,100)
b=len(A)
n=-1
while n!=0:
    n=int(input('''[ 1 ] Mostrar o vetor.
[ 2 ] Mostrar vetor na ordem inversa.
[ 0 ] Sair do programa.
Escolha uma Opção: '''))
    if n==1:
        print (A)
    elif n==2:
        print('[', end="")
        for c in range (b-1,-1,-1):
            print (f'{A[c]}', end="")
            print (', ' if c>0 else ']', end="")
        print()
    elif n>2 or n<0:
        print ('Valor inválido.')
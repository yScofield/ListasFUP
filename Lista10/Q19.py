def MA(x):
    soma=0
    for i in range (len(x)):
        soma+=x[i]
    return soma/len(x)

import random
vetor=[0]*15
for i in range(15):
    vetor[i]=random.randint(1,10)
n=-1
while n!=0:
    n=int(input('''[ 1 ] Mostrar vetor.
[ 2 ] Mostrar vetor ao contrário.
[ 3 ] Média aritmética.
[ 0 ] Sair do programa.
Escolha uma opção: '''))
    if n==1:
        print (vetor)
    elif n==2:
        print ('[', end="")
        for i in range (15-1,-1,-1):
            print (f'{vetor[i]}', end="")
            print (', ' if i!=0 else ']', end="")
        print()
    elif n==3:
        print (f'Média aritimética: {MA(vetor)}')
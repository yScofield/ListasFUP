def mfp(x):
    cont=2
    while x!=1:
        if x%cont==0:
            x=x/cont
        else:
            cont+=1
    return cont

x=int(input('Digite um número: '))
print(f'O maior fator primo de {x} é: {mfp(x)}')
frase = input('Digite uma frase: ')
cont=0
for c in frase:
    cont+=1
for c in frase:
    print (f'{frase[cont-1]}', end="")
    cont-=1
nome= input('Digite um nome: ')
nome = nome.split()
cont=0
n=0
for c in nome:
    print (f'{c}', end="")
    n+= len(nome[cont])
    cont+=1
print ('')
print (f'Esse nome tem {n} letras.')
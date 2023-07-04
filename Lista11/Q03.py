x=input('Digite o nome ou caminho de um arquivo: ')
with open(x,'r') as arquivo:
    n=arquivo.read()
    arquivo.close()
    cont=0
    n=n.lower()
    for i in n:
        if i in 'aeiou':
            cont+=1
    print (f'O arquivo tem {cont} vogais.')
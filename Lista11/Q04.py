arq=input('Digite o nome ou caminho do arquivo: ')
x=input('Digite o caractere que você procura: ')
with open(arq, 'r') as arquivo:
    n=arquivo.read()
    arquivo.close
    cont=0
    for i in n:
        if x in i:
            cont+=1
if cont>0:
    print (f'O caractere {x} aparece {cont} vez', end="")
    print ('es no arquivo.' if cont!=1 else ' no arquivo.')
else:
    print (f'O caractere {x} não aparece no arquivo.')
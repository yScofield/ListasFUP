arq=input('Digite o nome ou caminho de um arquivo: ')
with open(arq, 'r') as arquivo:
    n=arquivo.read()
    arquivo.close()
n=n.upper()
newarq=input('Digite o nome ou caminho do novo arquivo: ')
with open(newarq, 'w') as arquivo:
    arquivo.write(n)
    arquivo.close()
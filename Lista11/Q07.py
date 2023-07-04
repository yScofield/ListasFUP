arq=input('Digite o nome ou caminho de um arquivo: ')
palavra=input('Digite uma palavra para procurar dentro do arquivo: ')
with open(arq, 'r') as arquivo:
    n=arquivo.read()
    arquivo.close()
x=len(palavra)

print(x)
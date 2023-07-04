arq=input('Digite o nome ou caminho de um arquivo: ')
with open(arq, 'r') as arquivo:
    texto=arquivo.read()
    arquivo.close()
newtexto=''
for i in texto:
    if i in 'aeiouAEIOU':
        newtexto+='*'
    else:
        newtexto+=i
newarq=input('Escreva o nome ou caminho novo do arquivo: ')
with open(newarq, 'w') as arquivo:
    arquivo.write(newtexto)
    arquivo.close()
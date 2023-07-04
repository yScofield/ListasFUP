narq=input('Digite o nome do novo arquivo: ')
with open(narq,'r') as arquivo:
    cont=0
    for i in arquivo:
        cont+=1
    print(cont)
arquivo.close()
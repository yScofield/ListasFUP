x=input('Digite o nome ou caminho de um arquivo: ')
with open(x,'r') as arquivo:
        n=arquivo.read()
        cont=0
        for i in n:
            if 97<=ord(i)<=122:
                cont+=1
        print (cont)

'''Está contando quantas letras são minusculas.'''
def arvore(x):
    for i in range (x):
        print ((x-i)*' ', (2*(i+1)-1)*'*')

x=int(input('Digite o tamanho da arvore: '))
arvore(x)
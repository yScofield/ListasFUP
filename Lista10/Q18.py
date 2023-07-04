def FDN(P):
    fd=1
    for i in range (1,P+1,2):
        fd=fd*i
    return fd

x=int(input('Digite um valor: '))
y=FDN(x)
print (f'O fatorial duplo de {x} é: {y}')
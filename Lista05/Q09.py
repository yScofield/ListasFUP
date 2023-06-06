print ('Digite números inteiros e positivos.')
n1= int(input('Digite o primeiro numero: '))
n2= int(input('Digite o segundo numero: '))
mmc1=n1
mmc2=n2
if n1>0 and n2>0:
    print (f'O mmc de {n1} e {n2} é: ', end="")
    while n1!=n2:
        if n1<n2:
            n1+=mmc1
        elif n2<n1:
            n2+=mmc2
    print (n1)
else:
    print('Valor invalido.')
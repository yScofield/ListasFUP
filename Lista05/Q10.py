print ('Digite numeros inteiros e positivos.')
n1= int(input('Digite o primeiro numero: '))
n2= int(input('Digite o segundo numero: '))
c=2
mdc=1
if n1>0 and n2>0:
    print (f'O mdc de {n1} e {n2} é: ', end="")
    while c<=n1 and c<=n2:
        if n1%c==0 and n2%c==0:
            n1=n1//c
            n2=n2//c
            mdc*=c
        else:
            c+=1
    print (f'{mdc}')
n= int(input('Digite um valor para o calculo fatorial: '))
nf=n
f=1
if n>0:
    for c in range (1,n+1):
        f*=c
    print (f'{nf}! é igual a {f}.')
elif n==0:
    print ('0! é igual a 1.')
else:
    print ('Valor inválido.')
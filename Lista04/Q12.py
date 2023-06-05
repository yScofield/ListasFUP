n= int(input('Digite um valor: '))
f1=n
f=0
nf=1
if n==1:
    print (f'{n}! = {n}')
elif n==0:
    print (f'{n}! = 1')
elif n<0:
    print ('Valor inválido.')
else:
    while n>1:
        f=n*(n-1)
        n=n-2
        nf*=f
    print (f'{f1}! = {nf}')
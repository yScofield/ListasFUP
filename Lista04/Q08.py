c=1
n=0
cm=0
while c<=10:
    n1= int(input('Digite um número positivo: '))
    if n1>0:
        n=n+n1
        cm+=1
    c+=1
print (f'{n/cm:.2f}')
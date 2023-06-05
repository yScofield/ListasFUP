c=1
n=0
cm=0
while c<=10:
    n1= int(input(f'Digite um número positivo: '))
    if n1>0:
        n=n+n1
    else:
        c-=1
    c+=1
print (f'{n/10:.2f}')
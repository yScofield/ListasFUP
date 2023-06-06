n= int(input('Digite um numero inteiro positivo: '))
np=0
for c in range(n-1,0,-1):
    if n%c==0:
        np+=c
if np==n:
    print (f'{n} é perfeito, pois ', end="")
    for c in range(1,n):
        if n%c==0:
            print (f'{c} ', end="")
            print ('+ ' if c<n/2 else '= ', end="")
    print (np)
else:
    print (f'{n} não é perfeito.')
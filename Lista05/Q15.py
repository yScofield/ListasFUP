print ('Estes são os números de 4 digitos que possuem a característica pedida.')
for c in range(1000,10000):
    n1=c//100
    n2=c%100
    soma=n1+n2
    if soma**2==c:
        print (f'{c} ', end="")
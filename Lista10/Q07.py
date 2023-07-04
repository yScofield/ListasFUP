def somadealg(x):
    if x>0:
        soma=0
        while x>0:
            a=x%10
            x=x//10
            soma+=a
        return soma
    else:
        return 'Número Inválido.'
    
x=int(input('Digite um número: '))
if x>0:
    print(f'A soma dos algarismos de {x} é igual a: {somadealg(x)}')
else:
    print (somadealg(x))
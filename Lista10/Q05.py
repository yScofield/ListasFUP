def hipotenusa(a,b):
    h= (a**2+b**2)**(1/2)
    return h

a=int(input('Digite o valor do lado a: '))
b=int(input('Digite o valor do lado b: '))
c=hipotenusa(a,b)
print(f'O valor da hipotenusa dos catetos a({a}) e b({b}) é: {c}')
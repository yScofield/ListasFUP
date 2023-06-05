a = float(input('Digite a variável a: '))
b = float(input('Digite a variável b: '))
c = float(input('Digite a variável c: '))

if a!=0:
    D = b**2-4*a*c
    x1 = (-b+D**(1/2))/(2*a)
    x2 = (-b-D**(1/2))/(2*a)
    if D < 0:
        print ('Não existe raiz real.')
    elif D == 0:
        print (f'Raiz Única.\n{x1}')
    elif D > 0:
        print (f'Raiz 1: {x1}\nRaiz 2: {x2}')
else:
    print ('Não é equação do 2º Grau.')
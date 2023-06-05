n1= int(input('Digite um valor: '))
n2= int(input('Digite outro valor: '))
di=0
if n1>0 and n2>0:
    di=n1/n2
    print (f'O quociente inteiro de {n1}/{n2} é: {int(di)}')
else:
    print ('Valor inválido.')
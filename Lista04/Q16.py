n = int(input('Digite o tamanho de F: '))
f1= 1
f2= 0
if n<1:
	print ('Valor inválido.')
else:
	print (f'A sequencia de fibonnaci de tamanho {n} é: ')
	while n>0:
		f3= f1+f2
		print (f'{f1}', end=" ")
		f2=f1
		f1=f3
		n-=1
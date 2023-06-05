n= int(input('Digite um valor: '))
while n!=0:
	qd=n**2
	cb=n**3
	if n>0:
		rz=n**(1/2)
	else:
		rz='Não existe.'
	print (f'Quadrado: {qd}\nCubo: {cb}\nRaiz quadrada: {rz}')
	n= int(input('Digite um valor: '))
print ('Fim do programa')
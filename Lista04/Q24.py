n= int(input('Digite um valor: '))
mn=n
mr=n
while n>=0:
	if n<mn:
		mn=n
	if n>mr:
		mr=n
	n= int(input('Digite um valor: '))
print (f'Maior numero: {mr}\nMenor numero: {mn}')
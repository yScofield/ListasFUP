n= int(input('Digite um numero: '))
c=1
soma=0
print (f'A soma dos divisores de {n} é:', end="")
while c<n-1:
	if n%c==0:
		soma+=c
		print (f'{c}', end="")
		print (' + ' if c<n/2 else ' = ', end="")
	c+=1
print (soma)
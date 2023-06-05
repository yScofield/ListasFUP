n= int(input('Digite um valor: '))
for c in range (1, n+1):
	n= int(input(f'Digite o valor numero {c}: '))
	if c==1:
		mn=n
		mr=n
	elif mn>n:
		mn=n
	elif mr<n:
		mr=n
print (f'Maior: {mr}\nMenor: {mn}')
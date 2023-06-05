n= int(input('Digite um valor: '))
linha= 1
num= 1
while linha<=n:
	cont=1
	while cont<=linha:
		print (f'{num} ', end="")
		cont=cont+1
		num+=1
	linha = linha+1
	print ("")
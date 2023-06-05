x= int(input('Digite a base: '))
n= int(input('Digite o expoente: '))
s=1
if n<0:
	print ('Expoente inválido.')
elif n==0:
	print ('1')
else:
	for n in range (1, n+1):
		s*=x
	print (f'{s}')
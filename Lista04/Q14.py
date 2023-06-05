n = int(input('Digite um valor inteiro positivo: '))
c=1
div=0
while c<=n:
	if n%c==0:
		div+=1
	c+=1
if div == 2:
	print (f'{n} é numero primo.')
else:
	print (f'{n} nao é primo.')
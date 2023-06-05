n=1000
soma=0
while n > 0:
	if n%3==0 or n%5==0:
		soma += n
	n -= 1
print (f'{soma-1000}')
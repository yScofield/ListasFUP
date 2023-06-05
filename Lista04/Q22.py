n= int(input('Digite um valor positivo: '))
c=1
f=1
E=1
while c<=n:
	f*=c
	E+=1/f
	c+=1
print (E)
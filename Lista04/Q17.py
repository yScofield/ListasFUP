n1= int(input('Digite o primeiro valor: '))
n2= int(input('Digite o segundo valor: '))
imp=1
par=0
if n1>n2:
	n1,n2=n2,n1
while n1<=n2:
	if n1%2==0:
		par+=n1
	else:
		imp*=n1
	n1+=1
print (f'A soma dos numeros pares do intervalo é: {par}\nAmultiplicação dos numeros impares do intervalo é: {imp}')
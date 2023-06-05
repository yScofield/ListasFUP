A=[0]*10
B=[0]*10
for c in range (0,10):
	A[c]=float(input(f'Digite o {c+1}° valor: '))
	B[c]=A[c]**2
for c in range (0,10):
	print (f'{A[c]} ao quadrado é: {B[c]}')
A= [0]*10
mn=0
mr=0
for c in range (0,10):
	A[c]= float(input(f'Digite o {c+1}° valor: '))
	if A[c]==A[0]:
		mn=A[c]
		mr=A[c]
	elif A[c]<mn:
		mn=A[c]
	elif A[c]>mr:
		mr=A[c]
print (f'Maior: {mr}\nMenor: {mn}')
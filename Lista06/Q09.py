A=[0]*20
for c in range (0,20):
	A[c]=float(input(f'Digite o {c+1}° valor: '))
	if A[c]<0:
		A[c]=0
print (A)
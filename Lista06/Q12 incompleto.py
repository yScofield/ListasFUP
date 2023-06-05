A=[ ]*12
nn=0
soma=0
for c in range (0,12):
	A[c]= float(input(f'Digite o {c+1}° valor: '))
	if A[c]<0:
		nn+=1
	if A[c]>0:
		soma+=A[c]
print (nn)
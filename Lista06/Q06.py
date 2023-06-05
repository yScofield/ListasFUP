A=[0]*15
par=0
imp=0
for c in range (0,15):
	A[c]= int(input(f'Digite o {c+1}° valor inteiro: '))
	if A[c]%2==0:
		par+=1
	if A[c]%2==1:
		imp+=1
print (f'Tem {par} vetores pares.')
print (f'Tem {imp} vetores impares.')
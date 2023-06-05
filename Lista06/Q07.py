A=[0]*15
imp=0
cv=0
for c in range (0,15):
	A[c]= int(input(f'Digite o {c+1}° valor: '))
	if A[c]%2==1:
		imp+=1
impV= [0]*imp
for c in range (0,15):
	if A[c]%2==1:
		impV[cv]=A[c]
		cv+=1
print (impV)
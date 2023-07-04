import random
A=[0]*12
nn=0
soma=0
for c in range (0,12):
	A[c]= random.randint(-10, 10)
	if A[c]<0:
		nn+=1
	if A[c]>0:
		soma+=A[c]
print (A)
print (nn)
print (soma)
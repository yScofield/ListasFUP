import random
A=[0]*11
B=[0]*11
Bt=[0]*17
for i in range (17):
	Bt[i]=[0]*11
for i in range (11):
	A[i]=[0]*17
	B[i]=[0]*17
	for j in range (17):
		A[i][j]=random.randint(1,5)
		B[i][j]=random.randint(1,5)
		Bt[j][i]=B[i][j]
	print(A[i])
for i in range (17):
	print(Bt[i])
C=[0]*11
for i in range (11):
	C[i]=[0]*11
#for i in range (11):
	for j in range (11):
		for k in range (17):
			C[i][j]+=A[i][k]*Bt[k][j]
	print (C[i])
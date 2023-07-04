import random
A=[0]*11
B=[0]*11
C=[0]*11
for i in range (11):
	A[i]=[0]*15
	B[i]=[0]*15
	C[i]=[0]*15
	for j in range (15):
		A[i][j]=random.randint(1,200)
		B[i][j]=random.randint(1,200)
		if A[i][j]>B[i][j]:
			C[i][j]=A[i][j]
		else:
			C[i][j]=B[i][j]
	print(C[i])
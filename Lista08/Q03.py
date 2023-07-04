A=[0]*5
for i in range (5):
	A[i]=[0]*5
for i in range (5):
	for j in range (5):
		A[i][j]=i*j
	print (f'{A[i]}')
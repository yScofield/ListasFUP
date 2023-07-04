A=[0]*10
for i in range (10):
	A[i]=[0]*10
	for j in range (10):
		if i<j:
			A[i][j]=2*i+7*j-2
		elif i==j:
			A[i][j]=3*i**2-1
		else:
			A[i][j]=4*i*3-5*j*2+1
	print (A[i])
import random
mat=[0]*20
c=20
soma=0
for i in range (20):
	mat[i]=[0]*20
	c-=1
	cont=1
	for j in range (20):
		mat[i][j]=random.randint(1,10)
	for j in range (c):
		soma=soma+mat[i][i+cont]
		cont+=1
	print (mat[i])
print (soma)
import random
mat= [0]*4
for i in range(4):
	mat[i] = [0]*4
cont=0
for i in range(4):
	for j in range(4):
		mat[i][j]= random.randint(1,50)
		print(f'{mat[i][j]}', end=" ")
		if mat[i][j]>10:
			cont+=1
	print()
print(f'{cont} são maiores que 10.')
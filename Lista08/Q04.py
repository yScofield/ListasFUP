import random
mat=[0]*14
for i in range (14):
	mat[i]=[0]*32
	for j in range (32):
		mat[i][j]= random.randint(1,10000)
mr=mat[0][0]
lin=0
col=0
for i in range (14):
	for j in range (32):
		if mat[i][j]>mr:
			mr = mat[i][j]
			col=i
			lin=j
	print(mat[i])
print (f'Maior numero: {mr}\nLocalização: Linha {lin} e Coluna {col}')
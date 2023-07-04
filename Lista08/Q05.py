import random
x= int(input('Digite um valor entre 1 e 99: '))
mat=[0]*13
cont=0
for i in range(13):
	mat[i]=[0]*10
	for j in range (10):
		mat[i][j]=random.randint(1,100)
		if x==mat[i][j]:
			cont+=1
			print(f'O valor foi encontrado na linha {j} e coluna {i}.')
if cont==0:
	print ('Não encontrado.')
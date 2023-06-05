A=[0]*30
media=0
mn=0
mr=0
for c in range (0,30):
	A[c]= float(input(f'Digite a nota do {c+1}° aluno: '))
	media+=A[c]
media/=30
for c in range (0,30):
	if media>A[c]:
		mn+=1
	elif media<A[c]:
		mr+=1
print (f'Acima da média: {mr}\nAbaixo da média: {mn}')
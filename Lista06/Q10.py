A=[0]*15
soma=0
for c in range (0,15):
	A[c]= float(input(f'Digite a nota do {c+1}° aluno: '))
	soma+=A[c]
soma/=15
print (f'A média da turma é: {soma}')
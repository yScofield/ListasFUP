N=int(input('Digite a quantidade de alunos: '))
alunos={}
for i in range(N):
    nome=input(f'Digite o nome do {i+1}º aluno: ')
    matricula=int(input('Digite a matricula: '))
    curso=input('Digite o curso: ')
    alunos[nome]=[matricula, curso]
print (alunos)
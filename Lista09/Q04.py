import random
n=int(input('Digite a quantidade de alunos: '))
alunos={}
AP={}
RP={}
for i in range (n):
    nome=input('Digite o nome do aluno: ')
    matric= random.randint(100000, 999999)
    mf= random.randint(2,10)
    alunos[nome]=[matric, mf]
for i in alunos.keys():
    if alunos[i][1]>=5.5:
        AP[i]="Aprovado"
    else:
        RP[i]="Reprovado"
print (alunos)
print (AP, RP)
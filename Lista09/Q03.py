import random
n=int(input('Digite a quantidade de alunos: '))
alunos={}
for i in range(n):
    nome=input('Digite o nome do aluno: ')
    matric=random.randint(100000, 999999)
    AP1=random.randint(0,10)
    AP2=random.randint(0,10)
    AP3=random.randint(0,10)
#    matric=input('Digite a matricula: ')
#    AP1=int(input('Digite a nota da 1ª prova: '))
#    AP2=int(input('Digite a nota da 2ª prova: '))
#    AP3=int(input('Digite a nota da 3ª prova: '))
    media=(AP1+AP2+AP3)/3
    if media>=7.5:
        R="Aprovado"
    else:
        R="Reprovado"
    alunos[nome]=[matric, AP1, AP2, AP3, R]
    if i==0:
        mr=media
        mn=media
        mAP1=AP1
    else:
        if media>mr:
            mr=media
        if media<mn:
            mn=media
        if AP1>mAP1:
            mAP1=AP1
    print (alunos[nome])
print(f'''Maior média: {mr}
Menor média: {mn}
Maior nota AP1: {mAP1}''')
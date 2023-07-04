import random
n=int(input('Digite a quantidade: '))
dicio={}
procure = -1
for i in range (n):
        titulo=''
        for j in range (10):
            titulo+=chr(random.randint(65,90))
        ano=random.randint(1980,2023)
        autor=''
        for j in range (5):
            autor+=chr(random.randint(97,122))
        autor=autor.capitalize()
        dicio[titulo]=[autor, ano]
while procure!=0:
    procure=int(input('''[ 1 ] Mostrar todos os titulos.
[ 2 ] Procurar um titulo Específico.
[ 0 ] Sair do programa.
Escolha uma opção: '''))
    if procure==1:
        for i in dicio.keys():
            print (i)
    if procure==2:
        ptitulo=input('Digite o titulo que procura: ')
        if ptitulo not in dicio.keys():
            print(100*'=', '\nTitulo não encontrado.\n', 100*'=')
        elif ptitulo in dicio.keys():
            print (100*'=', f'\n{dicio[ptitulo]}\n', 100*'=')
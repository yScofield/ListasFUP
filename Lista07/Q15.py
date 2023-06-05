c=11
while c!=0:                                                    #Condição pro Fim do programa.
    print ('''Escolha uma opção e digite o respectivo número.
[ 1 ] Ler uma String de até 20 caracteres.
[ 2 ] Imprimir o tamanho da String digitada.
[ 3 ] Comparar a String anterior com uma nova String.
[ 4 ] Concatenar a primeira String com uma nova String.
[ 5 ] Imprimir a primeira String ao contrário.
[ 6 ] Contar quantas vezes um caractere aparece na primeira String.
[ 7 ] Trocar o primeiro caractere determinado pelo usuário por outro da primeira String.
[ 8 ] Verificar se uma substring esta contida na primeira String.
[ 9 ] Mostrar uma substring da primeira String determinada pelo usuário.
[ 0 ] Para sair do programa.''')
    c=int(input('Aguardando a escolha: '))
    if c==1:
        S1= input('Digite a primeira String: ')
    elif c==2:
        print (f'A String tem {len(S1)} caracteres.')
    elif c==3:
        S2= input('Digite a nova String para comparação: ')
        a=len(S1)
        b=len(S2)
        cont=0
        if a==b:
            s=0
            print ('As Strings têm o mesmo tamanho.')
            for r in S1:
                cont+=1
                if r==S2[s]:
                    cont-=1
                s+=1
            if cont==0:
                print ('As Strings são iguais.')
            else:
                print ('As Strings são diferentes.')
        else:
            print ('As Strings têm tamanhos diferentes e portanto, não são iguais.')
    elif c==4:
        S2= input('Digite uma nova String para juntar com a anterior: ')
        print (S1+' '+S2)
    elif c==5:
        a=len(S1)
        while a>0:
            print (f'{S1[a-1]}', end="")
            a-=1
            if a==0:
                print ('')
    elif c==6:
        S2= input('Digite um caractere para saber quantas vezes ele aparece na primeira String: ')
        a=S1.count(S2)
        print (f'O caractere "{S2}" aparece {a} vezes na primeira String.')
    elif c==7:
        C1= input('Digite um caractere para mudar da primeira String: ')
        C2= input('Digite um caractere para colocar no lugar: ')
        A=S1.replace(C1, C2, 1)
        print (A)
    elif c==8:
        S2= input('Digite algo para verificar se é substring da primeira String: ')
        A= S1.find(S2)
        b= len(S2)
        if A==-1:
            print ('Não é substring da primeira String.')
        elif b>1 and A!=-1:
            print (f'É substring da primeira String.\nInicia na posição {A+1} e termina na posição {A+b}.')
        elif A!=-1 and b==1:
            print (f'É substring da primeira String.\nEstá na posição {A+1}.')
    elif c==9:
        C1= int(input('Digite a posição de inicio da substring: '))
        C2= int(input('Digite a posição final da substring: '))
        if C1>C2:
            print ('A posição inicial tem que ser menor do que a final.')
        else:
            print (S1[C1-1:C2])
    print (100*'/')
    c= int(input('[ 10 ] Para voltar para as opções.\n[ 0 ] Para sair.\nDigite uma opção: '))
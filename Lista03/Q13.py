N1 = float(input('Digite um número: '))
Op = int(input('1.[+]  2.[-]  3.[*]  4.[/]\nEscolha uma opção: '))
N2 = float(input('Digite outro número: '))
R = 0
if Op==1:
    R = N1+N2
    print (f'[{R}]')
elif Op==2:
    R = N1-N2
    print (f'[{R}]')
elif Op==3:
    R = N1*N2
    print (f'[{R}]')
elif Op==4 and N2!=0:
    R = N1/N2
    print (f'[{R}]')
elif Op==4 and N2==0:
    print ('Não é Possível dividir por 0!')
else:
    print ('Operação Inválida.')
N1 = float(input('Digite um número: '))
N2 = float(input('Digite outro número: '))
Op = int(input('[1] Média entre os números.\n[2] Diferença do maior pelo menor.\n[3] Produto entre os números.\n[4] Divisão do 1º pelo 2º\nEscolha uma Opção: '))
Op1 = 0
Op2 = 0
Op3 = 0
Op4 = 0
if Op == 1:
    Op1 = (N1+N2)/2
    print (f'A média entre os números é: {Op1}')
elif Op == 2:
    Op2 = ((N1-N2)**2)**(1/2)
    print (f'A diferença do maior para o menor é: {Op2}')
elif Op == 3:
    Op3 = N1*N2
    print (f'A multiplicação entre {N1} e {N2} é: {Op3}')
elif Op == 4 and N2!=0:
    Op4 = N1/N2
    print (f'A divisão de {N1} por {N2} é {Op4}')
elif Op == 4 and N2==0:
    print ('Não é possivel dividir um número por 0.')
else:
    print ('Opção invalida.')
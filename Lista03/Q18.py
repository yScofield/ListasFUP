Ano = int(input('Digite um ano: '))

if Ano%400==0 or Ano%4==0 and Ano%100!=0:
    print (f'{Ano:.0f} é ano bisexto.')
else:
    print (f'{Ano:.0f} não é ano bisexto')
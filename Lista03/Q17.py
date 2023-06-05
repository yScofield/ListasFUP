I = float(input('Sua Idade: '))
TS = float(input('Seu Tempo de Serviço: '))

if I>=65 or TS>=30 or I>=60 and TS>=25:
    print ('Pode se aposentar.')
else:
    print ('Não pode se aposentar.')
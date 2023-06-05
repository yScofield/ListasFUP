Pn = float(input('Digite a posição inicial de Naruto: '))
Ps = float(input('Digite a posição inicial de Sasuke: '))
Vn = float(input('Digite a velocidade constante de Naruto: '))
Vs = float(input('Digite a velocidade constante de Sasuke: '))

if Pn > Ps:
    print ('O Naruto não pode estar na frente do Sasuke.')
elif Vn > Vs and Pn!=Ps:                                    # Fiz as variáveis dentro do 'elif' por que se eu faço fora e o usuário coloca os dois 
    t = (Ps-Pn)/(Vn-Vs)                                     # com a mesma velocidade constante a variável 't' teria que ser dividida por 0 e isso 
    Pf = Ps+Vs*t                                            # não é possivel.
    print (f'O Naruto irá alcançar o Sasuke no Km {Pf}')
elif Pn == Ps:
    print ('O Naruto já está na mesmo posição que o Sasuke.')
else:
    print ('Sasuke Chegou no Esconderijo do #Orochimaru.')
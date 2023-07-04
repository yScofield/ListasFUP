with open('Lista11/arq.txt', 'w') as arquivo:
    x=input('Digite "0" para encerrar o programa.\nDigite dentro do arquivo: ')
    x+='\n'
    while x!='0\n':
        arquivo.write(x)
        x=input('Digite "0" para encerrar o programa.\nDigite dentro do arquivo: ')
        x+='\n'
arquivo.close()
def verifsinal(x):
    if x<0:
        return -1
    if x==0:
        return 0
    if x>0:
        return 1

n=int(input('Digite um valor para verificar o sinal: '))
print (f'O valor retornado é: {verifsinal(n)}')
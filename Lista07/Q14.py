S= input('Digite uma frase: ')
cont=len(S)
I= int(input(f'Digite um numero de 1 à {cont}, para o inicio do segmento: '))
J= int(input(f'Digite um numero de {I} à {cont}, para o fim do segmento: '))
print (S[I-1:J])
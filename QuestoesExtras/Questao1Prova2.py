#Faça um programa que receba um número inteiro positivo x que deve ser digitado pelo usuário.
#Seu programa deve exibir na tela a decomposição em fatores primos do número x e quantas vezes cada fator aparece.
#Exemplo: Caso o numero digitado seja x = 60, então 60 pode ser decomposto em 2² x 3¹ x 5¹ = 60
#fator 2 aparece 2 vezes.
#fator 3 aparece 1 vez.
#fator 5 aparece 1 vez.

x = int(input('Digite um inteiro positivo: '))
f=2
cf=0
d=0
if x>0:
    while x>=1 and d!=2:
        if x%f==0:
            x=x//f
            cf+=1
        elif cf>1:
            print (f'Fator {f} aparece {cf} vezes.')
            f+=1
            cf=0
        elif cf==1:
            print (f'Fator {f} aparece {cf} vez.')
            f+=1
            cf=0
        else:
            f+=1
        if x==1:                                        
            d+=1                                        #contador para q o while repita uma unica vez quando x==1
else:
    print ('Valor inválido.')
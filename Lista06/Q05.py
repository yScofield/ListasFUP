A= [0]*15
for c in range (0,15):
	A[c]= float(input(f'Digite o {c+1}° valor: '))
x=int(input('Digite a primeira posição para a soma: '))
y=int(input('Digite a segunda posição para a soma: '))
soma=A[x-1]+A[y-1]
print (f'{A[x-1]} + {A[y-1]} = {soma}')
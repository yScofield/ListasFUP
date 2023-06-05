A=[0]*10
n=9
for c in range (0, 10):
	A[c]= int(input(f'Digite o {c+1}° valor: '))
while n>=0:
	print (f'{A[n]} ', end="")
	n-=1
n = int(input('Digite quantos valores vc quer: '))
mn=1
qn=0
while n>0:
	v = int(input('digite um valor: '))
	if mn<v:
		mn=v
		qn=0
	if mn==v:
		qn+=1
	n-=1
print (f'O maior numero é: {mn}\nA quantidade de aparições desse numero é: {qn}')
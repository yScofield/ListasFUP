n= int(input('Digite o valor do saque: '))
r100=0
r20=0
r2=0
if n>=100:
	while n>=100:
		r100+=1
		n-=100
	print (f'{r100} nota(s) de R$100,00.')
if n>=50:
	n-=50
	print ('1 nota de R$50,00.')
if n>=20:
	while n>=20:
		r20+=1
		n-=20
	print (f'{r20} nota(s) de R$20,00.')
if n>=10:
	n-=10
	print ('1 nota de R$10,00.')
if n>=5:
	n-=5
	print ('1 nota de R$5,00.')
if n>=2:
	while n>=2:
		r2+=1
		n-=2
	print (f'{r2} nota(s) de R$2,00.')
if n>=1:
	print ('1 nota de R$1,00')
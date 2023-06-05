c=1
while c!=5:
	c= int(input('[ 1 ] Soma\n[ 2 ] Subtração\n[ 3 ] Multiplicação\n[ 4 ] Divisão\n[ 5 ] Sair\nEscolha uma opção: '))
	if c<1 or c>5:
		print (20*'=', '\nValor inválido.\n', 20*'=')
	elif c>=1 and c<=4:
		n1= float(input('Digite o primeiro valor: '))
		n2= float(input('Digite o segundo valor: '))
		R=0
		v=0
		if c==1:
			R=n1+n2
		elif c==2:
			R=n1-n2
		elif c==3:
			R=n1*n2
		elif c==4 and n2==0:
			print ('Não é possivel dividir por 0.')
			print (50*'=')
			v+=1
		elif c==4 and n2!=0:
			R=n1/n2
		if v!=1:
			print (f'A resposta é: {R}')
			print (50*'=')
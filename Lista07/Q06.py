nome= input('Digite o seu nome: ')
sexo= int(input('[ 1 ] Masculino\n[ 2 ] Feminino\nDigite o número correspondente ao seu sexo: '))
idade= int(input('Digite a sua idade: '))
if sexo==2 and idade<25:
    print (f'{nome}\nEMPODERAMENTO')
else:
    print (f'{nome}\nEMPODERAR-SE')
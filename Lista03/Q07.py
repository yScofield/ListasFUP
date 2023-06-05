S1 = float(input("Digite o valor do salário: "))
P1 = float(input("Digite o valor da prestação: "))

if P1 > S1*0.2:
    print ("Empréstimo não concedido.")
else:
    print ("Empréstimo concedido.")
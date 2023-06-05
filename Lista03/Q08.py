N1 = int(input("Digite um número divisível por 3 ou 5 mas não pelos dois: "))

if (N1%3==0 or N1%5==0) and N1%15!=0:
    print ("É divisível por 3 ou por 5, mas não pelos dois.")
else:
    print ("Invalido.")
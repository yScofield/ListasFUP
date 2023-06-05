N1 = int(input("Digite um número de 100 a 999: "))

N2 = N1 % 10
N3 = (N1-N2)%100/10
N4 = (N1-N3*10-N2)%1000/100
R = N2*100+N3*10+N4
print ("O numero ao contrario é: %d" % R)
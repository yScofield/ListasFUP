N1 = int(input("Digite um numero de 1000 a 9999: "))
N2 = N1%10
N3 = N1%100-N2
N4 = N1%1000-N3-N2
N5 = N1%10000-N4-N3-N2

print ("{:.0f}\n{:.0f}\n{:.0f}\n{}\n".format(N5/1000, N4/100, N3/10, N2))
N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))

if N1 < 0 or N1 > 10:
    print ("Nota invalida.")
elif N2 < 0 or N2 > 10:
    print ("Nota invalida.")
elif N3 < 0 or N3 > 10:
    print ("Nota invalida.")
else:
    M = (N1+N2+N3)/3
    print (f"A média é: {M:.2f}")
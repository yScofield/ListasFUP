N1 = float(input("Digite o primeiro valor: "))
N2 = float(input("Digite o segundo valor: "))
N3 = float(input("Digite o terceiro valor: "))

if N1 >= N2 and N1 >= N3:
    print (f"O maior número é: {N1}")
elif N2 >= N1 and N2 >= N3:
    print (f"O maior número é: {N2}")
elif N3 >= N1 and N3 >= N2:
    print (f"O Maior Número é: {N3}")
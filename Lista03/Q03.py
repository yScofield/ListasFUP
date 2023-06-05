N1 = int(input("Primeiro número: "))
N2 = int(input("Segundo número: "))
N3 = int(input("Terceiro número: "))
N4 = int(input("Quarto número: "))
S = 0

if N1%2==0:
    S = N1
if N2%2==0:
    S = S + N2
if N3%2==0:
    S = S + N3
if N4%2==0:
    S = S + N4
print (f"A Soma dos números pares é: {S}")
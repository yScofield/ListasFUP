N1 = float(input('Primeiro Número: '))
N2 = float(input('Segundo Número: '))
N3 = float(input('Terceiro Número: '))

if N1>=N2>=N3:
    print (N3, N2, N1)
elif N1>=N3>=N2:
    print (N2, N3, N1)
elif N2>=N1>=N3:
    print (N3, N1, N2)
elif N2>=N3>=N1:
    print (N1, N3, N2)
elif N3>=N1>=N2:
    print (N2, N1, N3)
elif N3>=N2>=N1:
    print (N1, N2, N3)
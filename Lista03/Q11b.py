N1 = float(input('Primeiro Número: '))
N2 = float(input('Segundo Número: '))
N3 = float(input('Terceiro Número: '))

if N1 < N3:
    N1, N3=N3, N1
if N1 < N2:
    N1, N2=N2, N1
if N2 < N3:
    N2, N3=N3, N2

print (f'{N3}, {N2}, {N1}')
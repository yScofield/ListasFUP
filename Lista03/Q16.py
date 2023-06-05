A = float(input('Digite o lado A: '))
B = float(input('Digite o lado B: '))
C = float(input('Digite o lado C: '))
if A > 0 and B > 0 and C > 0:
    if A < B+C and B < A+C and C < A+B:
        if A==B and A==C:
            print ('Triângulo Equilátero.')
        elif A!=B and A!=C and B!=C:
            print ('Triângulo Escaleno.')
        elif A==B and A!=C or A==C and A!=B or B==C and A!=B:
            print ('Triângulo Isósceles.')
    else:
        print ('Não é triângulo.')
else:
    print ('Não é triângulo.')
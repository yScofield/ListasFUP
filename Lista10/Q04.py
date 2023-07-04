def quadperf(x):
    x=x**(1/2)

    if x==int(x):
        print('sim')
    else:
        print('não')

n=int(input('Digite um numero para verificar: '))
quadperf(n)
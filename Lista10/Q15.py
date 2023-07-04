def SAF(x):
    mf=1
    soma=0
    if x>0:
        for i in range (x,0,-1):
            mf*=i
        b=mf
        while b>0:
            a=b%10
            b=b//10
            soma+=a
        print(f'O fatorial de {x} é: {mf}')
        print(f'A soma dos algarismos de {mf} é: {soma}')
x=int(input('Digite um número: '))
SAF(x)
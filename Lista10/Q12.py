def Qnp(x):
    R=0
    for i in range(x):
        cont=0
        n=1
        while n<=i:
            if i%n==0:
                cont+=1
            n+=1
        if cont==2:
            R+=1
    return R
x=int(input('Digite um número: '))
print(f'O quantidade de números primos abaixo de {x} é: {Qnp(x)}')
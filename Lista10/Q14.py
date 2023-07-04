def DesTL(x):
    n=1
    while n<=x:
        print(n*'*')
        n+=1
    n=x
    while n>0:
        n-=1
        print(n*'*')

x=int(input('Digite a largura do triangulo: '))
DesTL(x)
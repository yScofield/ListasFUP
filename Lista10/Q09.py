def somaentre2(x,y):
    soma=0
    if x>y:
        a=y
        y=x
        x=a
    while x+1<y:
        soma+=x+1
        x+=1
        print(x, soma)
    return soma

n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))

print(somaentre2(n1,n2))
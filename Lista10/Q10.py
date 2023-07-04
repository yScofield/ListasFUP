def exp(x,z):
    mult=1
    while z>0:
        mult*=x
        z-=1
        print(mult)
#    print (mult)

x=int(input('Digite a base: '))
z=int(input('Digite o expoente: '))
exp(x,z)
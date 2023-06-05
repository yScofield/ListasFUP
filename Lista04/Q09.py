c=2
n=float(input('Digite um valor: '))
menor=n
maior=n
while c<=10:
    n = float(input('Digite um valor: '))
    if menor>n:
        menor=n
    elif maior<n:
        maior=n
    c+=1
print (f'Menor número:{menor}\nMaior número:{maior}')
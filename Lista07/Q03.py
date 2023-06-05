f1 = input('Digite algo: ')
f2 = input('Digite algo: ')
cont=0

for a in f1:
    cont+=1
for b in f2:
    cont-=1    
if cont == 0:
    c=0
    for a in f1:
        cont+=1
        print(cont)
        if a == f2[c]:
            cont-=1
            print (cont)
        c+=1
    if cont == 0:
        print ('As strings são iguais.')
    else:
        print ('As strings são diferentes.')
else:
    print ('As strings são diferentes.')
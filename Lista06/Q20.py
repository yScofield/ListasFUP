A=[0]*100
cont=0
n=1
while cont<100:
    if n%10!=7 and n%7!=0:
        A[cont]=n
        cont+=1
    n+=1
print (A)
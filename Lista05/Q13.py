print ('Estes são os números de 1000 a 1999 em que dividos por 11 dão resto 5.')
for c in range(1000,2000):
    if c%11==5:
        print (f'{c} ', end="")
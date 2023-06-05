frase= input('Digite algo: ')
for c in frase:
    a=ord(c)
    if a>96 and a<123:
        a=chr(a-32)
        print (f'{a}', end="")
    else:
        print (f'{c}', end="")
frase = input('Digite algo: ')
for c in frase:
    #a=ord(c)
    #if a!=65 and a!=69 and a!=73 and a!=79 and a!=85 and a!=97 and a!=101 and a!=105 and a!=111 and a!=117:
    if c!='a' and c!='e' and c!='i' and c!='o' and c!='u' and c!='A' and c!='E' and c!='I' and c!='O' and c!='U' and c!='ã' and c!='õ':
        #b=chr(a)
        print (f'{c}', end="")
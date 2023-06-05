frase = input('Digite algo: ')
vogais= [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
for c in frase:
    a=ord(c)
    if a!=65 and a!=69 and a!=73 and a!=79 and a!=85 and a!=97 and a!=101 and a!=105 and a!=111 and a!=117:
        b=chr(a)
        print (f'{b}', end="")
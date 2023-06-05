D = int(input('Digite a quantidade de Ratos Golpistas(Deputados): '))
S = int(input('Digite a quantidade de Roedores Golpistas(Senadores): '))

if D < 342:
    print ('Colocaram Fogo na Câmara dos DepuRatos e Evitaram o Golpe.')
elif D >= 342 and S < 54:
    print ('Homens Bombas Explodiram o Senado Federal e Evitaram o Golpe.')
else:
    print ('Nem Goku, nem Naruto e muito menos os Vingadores. Tome Golpe.')
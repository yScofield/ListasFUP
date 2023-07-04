import random
baralho={"cartas":['A','1','2','3','4','5','6','7','8','9','10','J','Q','K'],
         "naipe":['Copas','Espadas','Ouro','Paus']}
P1={}
P2={}

print('='*30,'Jogador 1','='*30)
for i in range(1, 6):
    m=random.randint(0,3)
    n=random.randint(0,13)
    P1[f'carta {i}']=f'{baralho["cartas"][n]} de {baralho["naipe"][m]}'
    print(P1[f'carta {i}'])
print()
print('='*30,'Jogador 2','='*30)
for i in range(1, 6):
    m=random.randint(0,3)
    n=random.randint(0,13)
    P2[f'carta {i}']=f'{baralho["cartas"][n]} de {baralho["naipe"][m]}'
    print(P1[f'carta {i}'])
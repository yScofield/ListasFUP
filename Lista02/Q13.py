QT = float(input("Digite o total de premiação em dinheiro: "))

G1 = QT * 0.46
G2 = QT * 0.32
G3 = QT - (G1+G2)

print ("Ganhador 1: {}\nGanhador 2: {}\nGanhador 3: {}".format(G1, G2, G3))
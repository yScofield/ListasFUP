x1 = float(input("Coordenada x do ponto a: "))
y1 = float(input("Coordenada y do ponto a: "))
x2 = float(input("Coordenada x do ponto b: "))
y2 = float(input("Coordenada y do ponto b: "))

Dist = ((x1-x2)**2+(y1-y2)**2)**(1/2)

print (f"A distancia entre o ponto a {x1,y1} e o ponto b{x2,y2} é: {Dist:.2f}")
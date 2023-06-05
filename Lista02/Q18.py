AP1 = float(input("Valor investido do apostador 1: "))
AP2 = float(input("Valor investido do apostador 2: "))
AP3 = float(input("Valor investido do apostador 3: "))
VPT = float(input("Valor do premio total: "))

APt = AP1+AP2+AP3
DPAP1 = AP1/APt*VPT
DPAP2 = AP2/APt*VPT
DPAP3 = AP3/APt*VPT

print (f"Ganhos do Apostador 1: R${DPAP1:.2f}\nGanhos do Apostador 2: R${DPAP2:.2f}\nGanhos do Apostador 3: R${DPAP3:.2f}")
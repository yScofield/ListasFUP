S = int(input("Digite um valor em segundos: "))
M = S//60
H = M//60
M0 = M-H*60
S0 = S-H*3600-M0*60
print ("{} Hora(s), {} Minuto(s) e {} Segundo(s).".format(H, M0, S0))

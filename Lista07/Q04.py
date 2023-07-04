nome = input('Digite um nome: ')
ns=nome.split()
A=len(ns)
nome=ns[0]
for i in range (1,A):
    nome+=ns[i]
print(A)
print(ns)
print (nome)
print (nome[0:6])
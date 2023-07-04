import random
A=[0]*10
n=9
for c in range (0, 10):
	A[c]= random.randint(0,10)
print (A)
print ('[', end="")
while n>=0:
	print (f'{A[n]}, ', end="")
	n-=1
print (']')
n = int(input('Digite o valor de n, sendo n >= k: '))
k = int(input('Digite o valor de k, sendo k >= 0: '))
nk=n-k
nf=1
kf=1
nkf=1
if n>0:
    for c in range (1, n+1):
        nf*=c
if k>0:
    for c in range (1, k+1):
        kf*=c
if nk>0:
    for c in range (1, nk+1):
        nkf*=c
if n==0:
    nf=1
if k==0:
    kf=1
if nk==0:
    nkf=1
if n<0 or k<0:
    print ('Valor inválido.')
if n>=0 and k>=0:
    cb= nf/(kf*nkf)
    print (f'O Coeficiente Binomial destes valores é: {cb}')
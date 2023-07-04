def data(d,m,a):
    if 0<d<10:
        y='0'+str(d)
    if 0<m<10:
        x='0'+str(m)
    print(f'Para a data: {y}/{x}/{a}')
    if m==1:
        m='Janeiro'
    elif m==2:
        m='Fevereiro'
    elif m==3:
        m='Março'
    elif m==4:
        m='Abril'
    elif m==5:
        m='Maio'
    elif m==6:
        m='Junho'
    elif m==7:
        m='Julho'
    elif m==8:
        m='Agosto'
    elif m==9:
        m='Setembro'
    elif m==10:
        m='Outubro'
    elif m==11:
        m='Novembro'
    elif m==12:
        m='Dezembro'
    print(f'Temos: {d} de {m} de {a}')

d=int(input('Dia: '))
m=int(input('Mês: '))
a=int(input('Ano: '))
data(d,m,a)
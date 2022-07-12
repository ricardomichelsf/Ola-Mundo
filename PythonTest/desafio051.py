p = int(input('Inicio: '))
r = int(input('Passo: '))
de = p + (10 - 1) * r
for c in range(p, de + r, r):
    print(c)
print('fim')

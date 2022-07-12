from math import hypot
ad = float(input('Digite o cateto adjacente: '))
op = float(input('Digite o cateto oposto: '))
hi = hypot(ad,op)
print(f'A hipoteenusa é {hi:.2f}')

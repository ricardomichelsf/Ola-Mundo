print('='* 10)
print('10 TERMOS')
print('='* 10)
inic = int(input('Primeiro termo: '))
ter = int(input('Razão: '))
deci = inic + (11 - 1) * ter
for c in range(inic, deci, ter):
    print(c, end=' -> ')
print('Fim')

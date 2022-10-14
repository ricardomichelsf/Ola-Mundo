numer = [[],[]]
nume = 0
for num in range(1, 7):
    nume = int(input(f'Digite o {num}° valor: '))
    if nume % 2 == 0:
        numer[0].append(nume)
    else:
        numer[1].append(nume)
print('-='*35)
numer[0].sort()
numer[1].sort()
print(f'Os valores pares são {numer[0]}')
print(f'Os valores impares são {numer[1]}')
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
par = mai = somcolu = 0
for pos in range(0, 3):
    for lo in range(0, 3):
        matriz[pos][lo] = int(input(f'Digite um valor para [{pos}, {lo}]: '))
        if matriz[pos][lo] % 2 == 0:
            par += matriz[pos][lo]
        if lo == 2:
            somcolu += matriz[pos][lo]
        if pos == 1:
            if matriz[pos][lo] > mai:
                mai = matriz[pos][lo]
print('-='*20)
for pos in range(0, 3):
    for lo in range(0, 3):
        print(f'[{matriz[pos][lo]:^5}]', end='')
    print()
print('-='*35)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valoes da terceira coluna é {somcolu}')
print(f'O maior valor da segunda linha é {mai}')

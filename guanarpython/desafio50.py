par = 0
con = 0
for c in range(1, 7):
    n1 = int(input(f'Digite o {c} valor: '))
    if n1 % 2 == 0:
        par = par + n1
        con += 1
print(f'O valor de todos os {con} números pares é {par}')

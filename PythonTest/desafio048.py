print('\033[1;36mSoma de números impares multiplos de 3 de 0 á 500')
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s += c
print('A soma de todos os {} valores solicitados é {}\033[m'.format(cont, s))
print("fim")

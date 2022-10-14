num = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = input("Quer continuar? [S/N] ").upper()
    if resp =='N':
        break
pares = []
impares = []
for numero in num:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Os numeros digitados foram {num}')
print(f'Os numeros pares digitados foram {pares}')
print(f'Os números impares digitados foram {impares}')
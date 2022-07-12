n = int(input())
soma = 0
denominador = 1
cont = 0
while not cont == n:
    soma += 1/(denominador ** 2)
    denominador += 1
    cont += 1
print(f'{soma:.6f}')

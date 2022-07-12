n = int(input())
soma = 0
denominador = 1
cont = 0
while not cont == n:
    if denominador % 2 == 0:
        soma += 1/denominador
        denominador += 1
        cont += 1
    else:
        soma += -1/denominador
        denominador += 1
        cont += 1
print(f'{soma:.6f}')

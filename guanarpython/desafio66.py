cont = som = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    som += num
print(f'Você digitou {cont} e a soma dos números é {som}')

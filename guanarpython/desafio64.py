cont = som = 0
num = int(input('Digite um número: '))
while num != 999:
    som += num
    cont += 1
    num = int(input('Digite um número: '))
print(f'Você digitou {cont} e a soma deles é {som}')
'''num = 0
digi = 0
som = 0
while num != 999:
    num = int(input('Digite um valor: '))
    if num != 999:
        digi += 1
        som += num
print(f'Você digitou {digi} e a soma deles é {som}')'''

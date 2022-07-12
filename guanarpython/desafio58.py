from random import randint
from time import sleep
palp = 0
lis = randint(0, 10)
print('\033[1m=\033[m'*33)
print('\033[1mVAMOS BRINCAR DE ADIVINHAÇÃO !!!!')
print('=\033[m'*33)
num = 11
while lis != num:
    num = int(input('Adivinhe onúmero de 0 até 10: '))
    print(f'Você digitou o número {num}')
    sleep(1)
    print('PROCESSANDO...')
    sleep(1)
    if num < lis:
        print('Mais... Tente outra vez.')
    elif num > lis:
        print('Menos... TEmte outra vez')
    else:
        print('PARABÉNS VOCÊ ACERTOU')
    palp += 1
print(f'Você precisou de {palp} tentaivas para vencer')

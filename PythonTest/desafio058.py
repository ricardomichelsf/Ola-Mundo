'''from random import randint
from time import sleep
n = 0
es = randint(0,10)
print('Adivinhe o número que pensei entre 0 e 10')
ad = int(input('O número pensado foi? '))
print('Processando....')
sleep(1)
while ad != es:
    if ad != es:
        print('Nâo, tente outra vez!!')
        n += 1
        ad = int(input('Foi? '))
        print('Processando....')
        sleep(1)
print('Você acertou Parabéns!!!')
print('Eu pensei no número {}'.format(es))
print('Você acertou mas precisou de {} tentativas!!'.format(n))'''
from random import randint
computador = randint(0, 10)
print('\033[32mAcabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!!\033[m'.format(palpites))

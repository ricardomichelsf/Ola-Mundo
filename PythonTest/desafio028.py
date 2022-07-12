from random import randint
from time import sleep
print('-='*28)
print('\033[36mVou pensar em um número entre 0 e 5. Tente Adivinhar...\033[m')
print('-='*28)
nu = int(input('Em que número eu pensei? '))
ad = randint(0,5)# faz o computador escolher um numero aleatorio entre os selecionados
print('PROCESSANDO...')
sleep(2)
if nu == ad:
    print('\033[1;4;36mPARABÉNS! Você venceu!!\033[m')
else:
    print('\033[1;4;36mVocê perdeu!!\ntente outra vez!!')
print('Eu pensei no número: {}\033[m'.format(ad))
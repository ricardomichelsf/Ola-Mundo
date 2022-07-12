from random import randint
from time import sleep
num = int(input('Adivinhe o número entre 0 e 5: '))
pen = randint(0, 5)
print('='*30)
print(f'Voce didigtou o número {num}')
sleep(0.3)
print('PROCESANDO....')
sleep(0.9)
if pen == num:
    print(f'Parabéns você adivinhou o numero {pen}')
else:
    print(f'Você errou eu pensei no número {pen}')


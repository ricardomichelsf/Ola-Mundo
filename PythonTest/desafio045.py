import random
from time import sleep
print('\033[36mVAMOS JOGAR JOKENPÔ\033[m')
jok = ['pedra', 'papel', 'tesoura']
esc = random.choice(jok)
adv = str(input('\033[33mEscolha:\033[m ')).strip()
print('\033[33mJJJJOOOOOOOOOO')
sleep(1)
print('KKEEEEEEENNNNN')
sleep(1)
print('PÔ')
print('=-'*20)
print(esc)
print(adv)
if adv == esc:
    print("Deu empate você escolheu {} e o computador {}".format(adv, esc))
elif adv == 'pedra' and esc == 'papel' or adv == 'tesoura' and esc == 'pedra' or adv == 'papel' and esc == 'tesoura':
    print('VOCÊ PERDEU KKK\nEu ganhei você escolheu {} e o computador {}'.format(adv, esc))
else:
    print('PARABÉNS\nVocê ganhou o computador escolheu {} e você {}'.format(esc, adv))
print('=-\033[m'*20)

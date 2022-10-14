from random import randint
from time import sleep
from operator import itemgetter
apostas = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)
}

print(f'<<='*4, 'Jogando dados', '=>>'*4)
for joga, apos in apostas.items():
    sleep(1)
    print(f'{joga:>10} tirou o número {apos} no dado.')

print()
print(f'<<='* 3, 'Classificação', '=>>'*3)

"""pos = 1
for jog in sorted(apostas, key= apostas.get, reverse=True):
    print(f'{pos:>6} lugar: {jog} com {apostas[jog]}.')
    sleep(1)
    pos += 1"""

ranking = []
ranking = sorted(apostas.items(), key=itemgetter(1), reverse=True)

for i , v in enumerate(ranking):
    print(f'{i+1:>5}° lugar: {v[0]} com {v[1]}.')
    sleep(1)

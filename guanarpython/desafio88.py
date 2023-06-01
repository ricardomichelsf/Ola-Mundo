from random import randint
from time import sleep
lista = []
jogo = []
print('-'*32)
print('        JOGA NA LOTOFACIL      ')
print('-'*32)
quant = int(input('Você quer fazer quantos jogos: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for indic, lis in enumerate(jogo):
    print(f'Jogo {indic+1:2}: {lis}')
    sleep(1)
print('-=' * 4, '< BOA SORTE! >', '-=' *4)
    

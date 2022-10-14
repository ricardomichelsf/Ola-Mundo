from random import randint
from time import sleep
print('\033[1:34:40mVAMOS JOGAR JOKENPÔ\033[m')
'''print("""Suas opçoes
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")
jog = int(input('Qual a sua jogada: '))
pedr = 'PEDRA'
pap = 'PAPEL'
tes = 'TESOURA'
quenp = [pedr, pap, tes]
esco = choice(quenp)
sleep(0.1)
print('JO')
sleep(0.4)
print('KEN')
sleep(0.4)
print('PO!!!')
print('='* 35)
if jog == 1:
    print(f'Você escolheu {pedr}')
    if esco == pedr:
        print(f'Eu tambem escolhi {esco} \033[1:30mEMPATAMOS\033[m')
    elif esco == pap:
        print(f'Eu escolhi {esco} \033[1:30mVENCI\033[m')
    elif esco == tes:
        print(f'Eu escolhi {esco} \033[1:30mPERDI\033[m')
elif jog == 2:
    print(f'Você escolheu {pap}')
    if esco == pap:
        print(f'Eu tambem escolhi {esco} \033[1:30mEMPATAMOS\033[m')
    elif esco == tes:
        print(f'Eu escolhi {esco} \033[1:30mVENCI\033[m')
    elif esco == pedr:
        print(f'Eu escolhi {esco} \033[1:30mPERDI\033[m')
elif jog == 3:
    print(f'Você escolheu {tes}')
    if esco == tes:
        print(f'Eu tambem escolhi {esco} \033[1:30mEMPATAMOS\033[m')
    elif esco == pedr:
        print(f'Eu escolhi {esco} \033[1:30mVENCI\033[m')
    elif esco == pap:
        print(f'Eu escolhi {esco} \033[1:30mPERDI\033[m')
else:
    print('\033[1:31m OPÇÃO INVÁLIDA!!!!\033[m')
print('='* 35)'''
itens = ('Pedra', 'Papel', 'Tesoura')
com = randint(0, 2)
opcao = 'S'
while opcao == "S":
    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    jog = int(input('Qual é a sua jogada? '))
    while jog > 2:
        print('\033[1:31mOPÇÃO INVÁLIDA\033[m')
        opcao = input('Quer jogar novamente [S/N]?: ').upper()
        jog = int(input('Qual é a sua jogada? '))
    sleep(0.2)
    print('JO')
    sleep(0.4)
    print('KEN')
    sleep(0.6)
    print('PO!!!')
    print('='* 30)
    print(f'Computador escolheu {itens[com]}')
    print(f'Você escolheu {itens[jog]}')
    print('='* 30)
    if com == 0:
        if jog == 0:
            print('\033[1mEMPATOU\033[m')
        elif jog == 1:
            print('\033[1mPERDI\033[m')
        elif jog == 2:
            print('\033[1mVENCI\033[m')
    elif com == 1:
        if jog == 0:
            print('\033[1mVENCI\033[m')
        elif jog == 1:
            print('\033[1mEMPATOU\033[m')
        elif jog == 2:
            print('\033[1mPERDI\033[m')
    elif com == 2:
        if jog == 0:
            print('\033[1mPERDI\033[m')
        elif jog == 1:
            print('\033[1mVENCI\033[m')
        elif jog == 2:
            print('\033[1mEMPATOU\033[m')
    opcao = input('Quer jogar novamente [S/N]?: ').upper()


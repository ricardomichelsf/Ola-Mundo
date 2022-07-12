cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezesete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digte um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Voce digitou o num {cont[num]}')
    else:
        print('Tente Novamente. ', end='')
    opc = input('Quer continuar? [S/N] ').strip().upper()
    if opc in 'Nn':
        break
    elif opc != 'S':
        opc = input('Quer continuar? [S/N] ').strip().upper()


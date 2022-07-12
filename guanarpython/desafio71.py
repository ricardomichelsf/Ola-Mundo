print('='*35)
print('          BANCO NENE')
print('='*35)
nu = int(input('Qual valor deseja sacar? R$ '))
while True:
    if nu >= 50:
        din = nu // 50
        nu = nu % 50
        print(f'Total de {din} cédulas de R$50')
        if nu % 50 == 0:
            break
    if nu >= 20:
        din = nu // 20
        nu = nu % 20
        print(f'Total de {din} cédulas de R$20')
        if nu % 20 == 0:
            break
    if nu >= 10:
        din = nu // 10
        nu = nu % 10
        print(f'Total de {din} cédulas de R$10')
        if nu % 10 == 0:
            break
    if nu >= 1:
        din = nu // 1
        print(f'Total de {din} cédulas de R$1')
        break
print('='*35)
print('Volte Sempre ao Banco NENE! Tenha um Bom dia')
'''valor = int(input("Que valor quer sacar? R$ ))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced> 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print("-"*30)
print("Volte Sempre")
    '''
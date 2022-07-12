km = float(input('Digite a distância em Km: '))
if km <= 200:
    valor = km * 0.5
    print(f'Sua viagem irá custar R$ {valor:.2f}')
else:
    valor = km * 0.45
    print(f'Sua viagem irá custar R$ {valor:.2f}')

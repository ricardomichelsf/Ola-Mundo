time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    partid = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for num in range(1, partid + 1):
        partidas.append(int(input(f'Quantos gols na partida {num}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRo, Digite s ou N!!')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('-='*30)
for ke, val in enumerate(time):
    print(f'{ke:>3} ', end='')
    for d in val.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados do jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<<'*7, 'VOLTE SEMPRE', '>>'*7)
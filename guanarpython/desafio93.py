jogador = {'nome': input('Nome do jogador: '),
        }

partid = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for num in range(1, partid):
    gol = int(input(f'Quantos gols na partida {num + 1}? '))
    gols.append(gol)

jogador['gols'] = gols[:]

jogador['total'] = sum(gols)

print('-='*29)
print(jogador)
print('-='*29)
for ke, val in jogador.items():
    print(f'O campo {ke} tem o valor {val}.')

print('-='*29)
print(f'O {jogador["nome"]} jogou {len(jogador["gols"])} partida.')

for part, gol in enumerate(jogador['gols']):
    print(f'   => Na partida {part+1}, fez {gol} gols')
print(f'Foi um total de {jogador["total"]} gols.')

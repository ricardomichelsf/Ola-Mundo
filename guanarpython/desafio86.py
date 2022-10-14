matri = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for posi in range(0, 3):
    for l in range(0, 3):
        matri[posi][l] = int(input(f'Digite um valor paraa posicao [{posi}, {l}]: '))

print('-='*25)
for posi in range(0, 3):
    for l in range(0, 3):
        print(f'[{matri[posi][l]:^5}]', end='')
    print()

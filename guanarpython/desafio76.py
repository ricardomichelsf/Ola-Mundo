listagem =('Lápis', 1.75,
           'Borracha', 2,
           'Cadreno', 15.00,
           'Estojo', 25,
           'Transferidor', 4.20,
           'Compasso', 9.99,
           'Mochil', 120.32,
           'Canetas', 22.30,
           'Livro', 34.90)
print('-'* 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'* 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'* 40)

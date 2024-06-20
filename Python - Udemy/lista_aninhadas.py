"""
Listas Aninhadas

- Algumas linguagens de programação possuem uma estrututa de dados chamadas de arrays:
    - Unidimenspnais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

Iterando com loops em listas aninhadas

num = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] # Matriz 3 x 3

print(num[0][1]) # 0
for n in num:
    print()
    for i in n:
        print(f'[ {i} ]', end='')

[[print(f'[ {valor} ]', end='') for valor in nu] for nu in num]
"""
num = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] 

# jogo da velha

velha = [['x' if numero % 2 == 0 else 'o' for numero in range(1, 4)] for numero in range(1, 4)]
print(velha)

for n in velha:
    print()
    for i in n:
        print(f'[ {i} ]', end='')
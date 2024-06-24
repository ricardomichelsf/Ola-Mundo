"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in) Agora temos
que importar e utilizar esta função a partir do modulo 'functools

Guido van Rossum: Utiliza a função reduce() se você realmente precisar. Em todo caso
99% das vezes um loop for é mais legível

Para enterder o reduce()

Imagine que você tem uma coleção de dados:

dados = [1, 2, 3, 4, 5]

E você tem uma função que recebe dois parâmetros

def funcao(x, y):
    return x * y
    
Assim com map() e filter(), a função reduce() recebe dois parâmetros: dunção e o iterável.
A função reduce() aplica a função passada como parâmetro ao primeiro e segundo elemento do
iterável, em seguida ao resultado e ao terceiro elemento, e assim por diante

vamos utilizar a função reduce() para multiplicar todos os numeros de uma lista


"""

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

n = 1 
for i in dados:
    n *= i

print(n)
# Ambas as formas produzem o mesmo resultado, mas a forma com o loop for é mais 
# legível e fácil de entender. A função reduce() é mais utilizada em casos mais
# complexos ou quando você precisa de uma forma mais concisa de resolver um problema.
# Em geral, é mais fácil de entender e manter um loop for do que uma função reduce
# com uma lambda function.
"""
Tuplas (tuple)

tuplas são bastante pareceidas com listas

Existem basicamente duas diferencas basicas

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são imutavéis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla.

# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento
tupla3 = (4, )
print(tupla3)
print(type(tupla3))

tupla4 = 4,
print(tupla4)
print(type(tupla4))

# Concluão: Podemos concluir que tuplas são definidas pelas virgulas e não pelo uso do parênteses

# Podemos gerar uma tupla dinamicamente
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla

print(escola)
print(curso)

# Soma, Valor Maximo, valor Minimo e Tamanho
# Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 = tupla1 + tupla2  # Tuplas são imutaveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla

tupla (1, 2, 3)
for n in tupla:
    print(n)

for indica, valor, in enumerate(tupla):
    print(indice, valor)

# Contamos elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)
print(escola('e'))

# Dicas na ultilização de tuplas
# Devemos utilizar tuplas Sempre que não precisarmos modificar  os dAados contidos
# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março','Aril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')

# Iterar com while

i = 0

while i < len(meses):
    print(meses[1])
    i += 1

# Verificando em qual indice um elemento esta na tupla

print(meses.index('Junho'))
# OBS: Caso o elemento não exista, será gerado ValueError

# Slicing
print(meses[5:9])

# O acesso a elementos de uma tupla também é semelahnte a de uma lista
print(meses[5])

# Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu codigo mais seguro.

# - Traabalhar com elementos imuitaveis traz segurança para o codigo.
# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla
print(nova)
print(tupla)
outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tupla)
"""




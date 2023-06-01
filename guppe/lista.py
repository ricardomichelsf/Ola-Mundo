"""
Lisras 

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINAMICO e tambem podermos colocar tipo de dados.

Linguagens C/Java: Arrays
    - Possui tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se voce criar um array do tipo int e com tamanho 5, este array sera
    Sempre do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python;
- Dinamica: Não possui tamanho fixo; ou seja. podemos criar a lista e simplismente ir adicionando elementos;
- Qualquer tipo de dado; Não possuem tipo de dado fixo; ou seja. poodemos colocar qualquer tipo de dado.
As listas em Python são representadas por colchetes: []

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1 ,44, 42, 27]

lista2 = ['a', 'A', 'b', 'B', 'c', 'C']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor esta contido na lista
num = 8
if num in lista4:
    print(f"Encontrei o numero {num}")
else:
    print(f"Não encontrei o numero {num}")

#Podemos facilmente ordernar uma lista

lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count("e"))

# Adicionar elementos em listas

Para adicionar elementos em listas, utilizamos a função append
OBS: Com append, nós só conseguimos adicionar 1 elemneto por vez
lista.append(42, 34, 56) # Erro

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 11]) # Coloca a lista como um elemento único
print(lista1)

if [8, 3, 11] in lista1:
    print("Encontrei a lista")
else:
    print('Nao encontrei a lista')

lista1.extend(123, 44, 67) # Coloca cada elemento da lista como valor adicional a lista
print(lista1)

Podemos inserir um novo elemento na lista informando a posição do indice
OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, "Novo valor")
print(lista1)

#Podemos facilmente juntar duas listas
lista1 += lista2
print(lista1)

# podemos facilmente inverter uma lista
forma 1
lista1.reverse()
lista2.reverse()
foram 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementeos existem dentro da lista
print(len(lista5))

# Podemos remover facilmente o último elemento de uma lista
OBS: O pop não somente remnove um elemento como tambem o retorna
print(lista5)
lista5.pop()
print(lista5)

Podemos remover um elemneto pelo indice
lista5.pop(2)
print(lista5)

Podemos zerar uma lista 
lista5.clear()
print(lista5

Podemos fcilmente repetir elementos em uma lista
nova = [1, 2, 3]
nova *= 3
print(nova)

Podemos facilmente converter uma string para lista

Exemplo 1

curso = 'Programação em Python Essencial'
print(curso)
curso = curso.split()
print(curso)

# Convertendo lista em strings

lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista, coloca espaço entre cada elemento e transforma em uma string
curso = " ".join(lista6)
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca cifrao entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2, 3, True, False, 'nene', 'Ricardo', [1, 2, 3], 45.1256465646]
print(lista6)
print(type(lista6))

# Iterando sobre lista

# Exemplo 1 - Utilizando for

soma = 0
for elemento in lista4:
    print(elemento)
    soma += elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair:  ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variaveis em listas

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros1 = [num1, num2, num3, num4, num5]
print(numeros1)

# Fazemos acesso aos elementos de forma indexada

#            0        1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

cores = ['verde', 'amarelo', 'azul', 'branco']
# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append[42]
lista.append[42]
lista.append[33]
lista.append[33]
lista.append[37]

print(lista)

# Outros métodos não tão importantes mas também úteis

# Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice da lista esta o valor 6?
print(numeros.index(6))

# Em qual indeice da lista esta o vlaor 9?
print(numeros.index(9))

# Obs: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de uma range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))
print(numeros.index(5, 2))

# Podeomos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) # Buscar o indice do valor 8, entre os inidce 3 a 6

# REvisão de slicing

# lista[inicio:fin:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o paramentro 'inicio

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parametro fim
print(lista[:2])

print(lista[:4])

print(lista[1:3])

# trabalhando com slice de lista com o arametro passo

print(lista[1::2]) # Começa no 1, vaoi ate o final de 2 em 2

# Invertendo valores em uma lista

nome = ["Geek", "University"]

nome[0], nome[1] = nome[1], nome[0]

print(nome)

nome.reverse()
print(nome)

# Soma, Valor Maximo, Valor Minimo, Tamanho

# Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# transformar uma lista em tupla

lista = [1, 2, 3, 4, 5]
print(type(lista))

valor = tuple(lista)
print(valor)
print(type(valor))

# Desempacotamento de lista

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1  Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)

"""

# Forma 2  Shallow Copy

lista = [1, 2, 3]

nova = lista # copia

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a copia via atribuição e copiamos os dados  da lista para a nova lista, mas
# apos realizar a modificacao em uma das listas , essa modificação se refletiu em ambas as listas.
# Isso em Python se chama Shallow copy


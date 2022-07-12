"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estrutura

C ou Java

for(int = 0 ; i < 10; i++){
    //execuçao do loop
}

Python

for item in interavel;
    //execucao do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis.

Exemplos de iteraveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range[1, 10]

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #Temos que transformar em lista

#Exemplos de for i
for letra in nome:
    print(letra, end='')

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)

OBS: o valor final não é incluido.
0
1
2
3
4
5
6
7
8
9

for numero in range(1, 10):
    print(numero)

for i, v in enumerate(nome):
    print(nome[i])

qtd = int(input('Quantas vezes esse loop deve rodar: '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'A soma é {soma}')
"""

for num in range(1, 11):
    print(f'\U0001F60D' * num)

for num in range(11, 0, -1):
    print(f'\U0001F60D' * num)
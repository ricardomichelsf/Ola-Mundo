"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências númericas, não de forma aleatória.
mas sim de maneira especoficada.

Formas gerais:

# Forma 1

range (valor_de_parada)

OBS: valor_de_parada não inclui(inicio padrão 0, e passo de 1 em 1)

# Exemplo Forma 1:
for num in range(11);
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_inicio indicado pelo usuario, passo de 1 em 1

Exemplo 2
for num in range(4, 11):
    print(num)

# Forma 3

range(valor_inicio, valor_parada, passo)

OBS: inicio indicado pelo usuario e passo indicado pelo usuario

Exemplo 3
for num in range(5, 55, 5):
    print(num)

Forma 4 (inversa)

range(valor_inicio, valor_parada, passo)
OBS: Forma decrescente

Exemplo 4
for num in range(10, 0, -1):
    print(num)
"""
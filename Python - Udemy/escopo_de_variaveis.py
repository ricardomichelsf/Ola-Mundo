"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o progrma.

2 - Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    esta limitado ao blooco onde foi declarada.


Para declara variáveis em Python fazemos:

nome_da_variavel = valor da variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
so declaramos uma variável, nós não colocamos o tipo de dadodela.
Esste tipo é inferido ao atribuírmos o valor a mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

numero = 42  # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existe = 'Oi'
print(nao_existe)

numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10  # A vaariável 'novo' está declarada localmente dentro do bloco do if, 
    # Portanto, é local
    print(novo)

print(novo)
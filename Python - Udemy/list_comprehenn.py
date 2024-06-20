"""
List Comprehension

- Utilizando list comprehesion podemos gerar novas listas com dados processadks a partir de outro iteravel

# Sintaxe da List Comprehension

[ dado for variavel in iteravel ]

# Exemplos

numeros = [1, 2, 3, 4, 5]
quadrado = [n * 10 for n in numeros]
print(quadrado)

Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte : for numero in numeros
- A segunda parte : n * 10

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

nome = 'Geek University'
print([letra.upper() for letra in nome])
amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo.capitalize() for amigo in amigos])
print([numero * 3 for numero in range(1, 10)])
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
print([str(numero) for numero in [1, 2, 3, 4,5]])

Podemos adicionar estruturas condicionais lógicas as nossas List Comprehension

"""
numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Qualquer número par modulo de 2 é 0 e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número impar modulo de 2 é 1 e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)


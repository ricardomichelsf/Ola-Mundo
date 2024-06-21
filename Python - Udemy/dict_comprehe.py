"""
Dictionary Comprehension

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

Sintaxe 

{chave: valor for variavel in iteravel}

Exemplo

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

numeros = [1, 2, 3, 4, 5]

quadrado = {valor: valor ** 2 for valor in numeros} 

print(quadrado) 

chaves = 'abcde'
numero = [1, 2, 3, 4, 5]
dicionario = {chave: valor for chave, valor in zip(chaves, numero)} # 
print(dicionario)

mistura = {chaves[i]: numero[i] for i in range(0, len(chaves))}
print(mistura)

Exemplo Llogica condicional

"""
numero = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numero}
print(res)
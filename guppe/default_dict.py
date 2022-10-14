"""
Modulo Collections - Default Dict

# Recap dicionario

dicionario = {'curso': 'Programação em python: Essencial'}
print(dicionario)
print(dicionario['outre']) # KeyError

Default Dict -> Ao criar um dicionario utilizando-o, nos informamos um valor default.
podemos utilizar um lambda para isso. Este valor será utilizando sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor
default será atribuido.

OBS: Lambda são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores;


"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
print(dicionario['outro']) # KeyError no dicionario comum, mas aqui não, ele ira adcionar o valor atribuido na função lambda
print(dicionario)
''

"""
Modulo Collections - Named Tuple

Named Tuple -> São tupla, diferenciadas, onde especificamos um nome para a mesma e tambem parametros.

"""

from collections import namedtuple

# Precisamos definir o nome e parametro.
# Fomra 1 - Declaração Named Tuple
cachorro = namedtuple('cahorro', 'idade raca nome')

# Fomra 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Fomra 3 - Declaração Named Tuple
cachorro =  namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade = 2, raca = 'Chow-chow', nome = 'Ray')
print(ray)

# Acessando os dados
# Forma 1

print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-chow'))
print(ray.count('Chow-chow'))


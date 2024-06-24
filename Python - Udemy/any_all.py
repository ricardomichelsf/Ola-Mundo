"""
Any e All

All() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável esta vazio
Any() -> Retorna True se pelo menos um elemento do iterável for verdadeiro, se o iterável estiver vazio retorna False

"""
# Exemplo com All()
print(all([True, True, True]))  # True
print(all([True, False, True]))  # False
print(all([]))  # True
print(all([1, 2, 3]))  # True
print(all([1, 2, 0]))  # False
print(all([1, 2, '']))  # False
print(all([1, 2, 'a']))  # True
print(all([1, 2, None]))  # False
print(all([1, 2, []]))  # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))  
# OBS: um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra not in 'aeiou']))

# Exemplo com Any()
print(any([True, True, True]))  # True
print(any([True, False, True]))  # True
print(any([]))  # False
print(any([1, 2, 3]))  # True
print(any([1, 2, 0]))  # True
print(any([1, 2, '']))  # True
print(any([1, 2, 'a']))  # True
print(any([1, 2, None]))  # True
print(any([1, 2, []]))  # True

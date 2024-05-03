"""
Modulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.

"""
from collections import deque

deq = deque('geek')
print(deq)

# Adicionando elementos no deque

deq.append('y') # Adiciona no final
print(deq)

deq.appendleft('k') # Adiciona no começo
print(deq)

# Remove elementos
print(deq.pop()) # Remove e retorna o ultimo elemento
print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento
print(deq)


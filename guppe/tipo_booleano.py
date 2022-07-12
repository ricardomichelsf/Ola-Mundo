"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeirao ou False

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula

Errado:

true, false

Certo:

True, False
"""

ativo = False

print(ativo)

"""
Operações básicas
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado sera falso.
se for falso o resulatado sera verdadeiro. Ou seja, sempre ao contrário
"""
print(not ativo)

logado = False

# Ou (or):
"""
È uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros

True or True -> True
True or False -> False
False or True -> False
False or False -> False
"""

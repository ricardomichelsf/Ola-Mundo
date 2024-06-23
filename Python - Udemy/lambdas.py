"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente lambdas, são funções sem nome, ou seja funções anônimas.

Expressão Lambda
calc = lambda x: 3 * x + 1
print(calc(4))

Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' '+ sobrenome.strip().title()
print(nome_completo('   joão   ', 'silva   '))

Em funções Python podemos ter nenhuma ou várias entradas. Em lambda também
amar = lambda: 'Como não amar Python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Helbert', 'Orson Scott Card', 'Douglas Adams',
           'H. G. Wells', 'Leigh Brackett']

# coloca em ordem pelo sobrenome que é sempre o último nome e coloca em ordem crescente
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower()) 
print(autores)

Funções quadráticas
f(x) = a * x ** 2 + b * x + c

Definindo a função

"""
def geradora_funcao_quadratica(a, b, c):
    '''Retoena a função f(x) = a * x ** 2 + b * x + c'''
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)


print(teste(0))
print(teste(1))
print(teste(2))  

print(geradora_funcao_quadratica(3, 0, 1)(2))
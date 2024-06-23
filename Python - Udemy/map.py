"""
Map 

Com map, fazemos mapeamento de valores para função

import math

def area(r):
    '''Calcula a área de um círculo com raio r'''
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]
# Map é uma função que recebe dois parâmetros: o primeiro a função, o segundo um iteravel
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Map com lambda
print(list(map(lambda r: math.pi * (r **2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização ela zera
# Por isso é comum converter para lista ou outro tipo de dados

# Para fixar - Map
# Temos dados iteráveis: dados: a1, a2, ...an
# Temos uma função: Função: f(x)
# Utilizamos a função map(f, dados) para aplicar a função f a cada elemento dos dados e obter um novo iterável com os resultados
# Map Object: f(a1), f(a2), f(....), f(an)

Exemplo


"""
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Llos Angeles', 26), ('Tokio', 27), ('Nova York', 28), 
           ('Londres', 22)]

print(cidades)

#lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))

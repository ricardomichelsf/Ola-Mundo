"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção

# Biblioteca para trabalhar com dados estatísticos

import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media:.2f}')

# OBS: Assim como o função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iteravel

res = filter(lambda x: x > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluidos da meméria

paises = ['', 'Argentina', '', 'Brasil', 'Chile', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
res = filter(None, paises)
res = filter(lambda pais: len(pais) > 0, paises)
res = filter(lambda pais: pais != '', paises)
print(list(res))  # Filtra os dados que não são vazios

A diferença entre map() e filter() é:
map() -> REcebe dois parâmetros, uma função e um iterável e retorna um objeto mapeado a função para cada elementp do iterável
filter() -> REcebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elemetos de acordo com a função

Exemplo:

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []}
]

# Filtrar os usuários que estão inativos np Twiter
res = filter(lambda vazio: len(vazio['tweets']) == 0, usuarios)
print(list(res))
res = filter(lambda vazio: not vazio['tweets'], usuarios) # ele vai pegar todos os valores false e filtrar pois toda lista vazia gera false
print(list(res))

Combinar filter() e map()

"""
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)

"""
Dicionarios
OBS: Em algumas linguagens de programação, os dicionarios Pythoon são conhecidos
por mapas.
Dicionarios são coleções do tipo chave/valor.
Dicionarios são representados por chaves {}.
OBS: Sobre dicionarios
    - Chave e valor são separados por dois pontos 'chave':'valor';
    - Tanto chave quanto valor ´pdem ser de qualquer tipo de dado;
    - Podemos misturaar Tipos de dados;

#Criação de dicionarios

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai)

# Acessando elementos

# Forma 1 - Acessando via chave 

print(paises['br'])
print(paises['ru'])
ObS: Se tentar localizar uma chave que nao exista sem o 'get' vai dar o erro KeyError.

# Forma 2 - Acessando via get - Recomendada

print(paises.get['br'])
print(paises.get['ru'])
@ Caso o get nao encontre o objeto com a chave inforamda será retornado o valor None e não sera gerado KeyErros.

# Podemos definir uma valor padrão para caso nao encontremos o objeto com a chave informada
pais = paises.get('py', Não encontrado)
print(f'Encontrei o {pais}')

3 Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado int, float, string, boolean, inclusive lista, tupla, dicionario como chabes de um dicionarios.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionarios. pois as mesma são imuitaveis.

localidades = {
    (35.6895, 39.6917) : 'Escritorio em Tokio',
    (40.7120, 74.0060) : 'Escritorio em Nova York',
    (37.7749, 122.4194) : 'Escritorio em São Paulo,
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario

receita = {'jan' : 100, 'fev' : 170, 'mar' : 300}
print(receita)

# Forma 1 - Mais comum
receita['abr] = 350
print(receita)

#Forma 2 

novo_dado = {'mai' : 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicioanrio

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.update ({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma.
# CONCLUSÂO 2: Em dicionarios , NÂO podemos ter chaves repetidas.

# Remover dados de um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.  

# Forma 2

del receita['fev']
print(receita)

# ONS: Neste caso o valor removido não é retornado

# Imagine que você tem um comercio eletrônico,  onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;

# 1 - Poderiamos utilizar uma lista para isso ? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300]
produto2 = ['Gos of war', 1, 150]

carrinho.append[produto1]
carrinho.append[produto2]

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos usar Tuplas para isso? Sim

produto1 = ('Playstation 4', 1, 2300)
produto2 = ('Gos of war', 1, 150)

carrinho = (produto1, produto2)

print(carrinho)

# 3 - Poderiamos usar Dicionarios para isso ? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300}
produto2 = {'nome':'Gos of war', 'quantidade': 1, 'preço': 150}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter certeza sobre cada informação.

# Metodos de dicionarios

d = dict(a=1, b=2, c=3)
print(d)

# Limpar o dicionario (Zerar dados )
d.clear()
print(d)

# Copiando um dicionario para outro
# Forma 1 - Deep copy

novo = d.copy() 
print(novo)
novo['d'] = 4

# Forma 2 - Shallow copy

novo = d
print(novo)

novo['d'] = 4
print(novo)
print(d)

# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O metodo fromkeys recebe dois parametros: interavel e um valor
# Ele vai gerar para cada valor do interavel uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)

# Interar sobre dicionarios
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')


# Acessando as chaves

print(recitas.keys())

for chave in receita.keys():
    print(chaves)

# Acessando os valores

print(receita.value())

for valor in receita.value():
    print(valor)

# Desempacotamento do Dcicionarios

print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

clientes = {
    'cliente1' : {
        'nome' : 'Luiz',
        'sobrenome' : 'Otavio'
    },
    'cliente2' : {
        'nome' : 'Ricardo',
        'sobrenome' : 'Michel'
    },
    'cliente3' : {
        'nome' : 'Maria',
        'sobrenome' : 'Moreira'
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}') # \t -> deixa o texto identado quando mostra na tela


perguntas = {
    'Pergunta 1' : {
        'pergunta' : 'Quanto é 2 + 2 ?',
        'resposta' : {'a' : '1','b' : '4','c' : '5',},
        'resposta_certa' : 'b',
    },
    'Pergunta 2' : {
        'pergunta' : 'Quanto é 3 * 2 ?',
        'resposta' : {'a' : '4','b' : '10','c' : '6',},
        'resposta_certa' : 'c',
    },
    'Pergunta 3' : {
        'pergunta' : 'Quanto é 144 / 12 ?',
        'resposta' : {'a' : '12','b' : '14','c' : '16',},
        'resposta_certa' : 'a',
    },
    'Pergunta 4' : {
        'pergunta' : 'Quanto é 9 * 7 ?',
        'resposta' : {'a' : '58','b' : '75','c' : '63',},
        'resposta_certa' : 'c',
    }
}

print()
print('Texto explicativo')
respostas_certas = 0
for pergunta_key, pergunta_value in perguntas.items():
    print(f'{pergunta_key}: {pergunta_value["pergunta"]}')

    print('Respostas: ')
    for resposta_key, resposta_value in pergunta_value['resposta'].items():
        print(f'{resposta_key}:{resposta_value}')

    resposta_usuario = input('Qual a resposta certa? ')

    if resposta_usuario == pergunta_value['resposta_certa']:
        print('Parabéns você acertou')
        respostas_certas += 1
    else:
        print('XIIIII, Você errou')

    print()

qtd_perguntas = len(perguntas)
porcetagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcetagem_acerto}')

"""

receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)

print(receita.keys())

for chave in receita.keys():
    print(chave)
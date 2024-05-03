"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia á Teoria dos conjuntos da Matematica.

- Aqui no Python os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matematica:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados  em Python com chaves{}

Diferença entre Conjuntos (Set) e Mapas (Dicionarios) em Python;
    - Um dicionario tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1 

s = set{(1, 2, 3, 4, 5, 5, 6, 7, 2, 3)} # Repare que temos valores repetidos.

print(s)
print(type(s))

@ OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error e não fará parte do conjunto.

# Foram 2 - mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# podemos verificar se determinado elemento esta contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não temo o 3')

# importante lembrar que, além de não termos valores duplicados, não temos ordem

lista = [99, 2, 34, 23, 12, 1, 44, 5]
print('Lista: {lista})

tupla = 99, 2, 34, 23, 12, 1, 44, 5
print('Tupla: {dados})

dicionario =  {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5], 'dict')
print('Dicionario: {dados}')

conjunto = {99, 2, 34, 23, 12, 1, 44, 5}
print('Conjunto: {conjunto}')



"""
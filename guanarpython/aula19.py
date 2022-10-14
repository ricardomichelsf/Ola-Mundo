"""pessoas = {'nome': 'Ricardo', 'sexo': 'M', 'idade': 22}
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
pessoas['peso'] = 99
for k in pessoas.keys():
    print(k)
print()
for v in pessoas.values():
    print(v)
print()
pessoas['nome'] = 'Nene'
for k, v in pessoas.items():
    print(f'{k}: {v}')
estado1 = {'uf': 'Rio de jameiro', 'sigla': 'rj'}
estado2 = {'uf': 'São Paulo', 'sigla': 'sp'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

loja = {
    'vendedor1': { # Posso adicionar dicionarios com input dentro de dicionarios criando assim varios dicionarios internos 
        'nome': 'Ricardo',
        'cargo': 'vendedor',
        'salario': 2800
    }
}
print(loja['vendedor1']['nome'])

"""

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())
for est in brasil:
    for ke, va in est.items(): # a variavel que for colocada no "for" ira percorrer o dicionario dentro da lista no segundo "for"
        print(f'O campo {ke} tem valor {va}')


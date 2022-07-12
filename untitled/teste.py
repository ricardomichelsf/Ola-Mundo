"""pessoas = {'nome': 'Ricardo', 'sexo': 'M', 'idade': 32}
pessoas['nome'] = 'Michel'
pessoas['peso'] = 129.00
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} abos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
          'Denise': [9.0, 8.5],
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}

for k, n in alunos.items():
    print(f' {k} : {max(n)}')"""

lista = ['a', 2, 'b', 'a', 'a']
#lis = 0
for pos, let in enumerate(lista):
    if let == 'a':
        print(f'{pos}', end='. ')
#print(lis)
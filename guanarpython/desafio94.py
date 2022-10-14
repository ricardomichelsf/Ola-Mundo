pessoas = {}
cadastro = []
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = input('Nome: ')
    while True:
        pessoas['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro, Digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    cadastro.append(pessoas.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()
        if resp in 'NS':
            break
        print('Erro, Digite S ou N')
    if resp in 'N':
        break
print('-='*35)
print(f'Foram cadastradas {len(cadastro)} pessoas')
media = soma / len(cadastro)
print(f'A media das pessoas cadastradas é {media}')
print(f'As mulheres cadastradas foram: ', end='')
print()
for pesso in cadastro:
    if pesso['sexo'] in 'Ff':
        print(f'{pesso["nome"]} ', end='')
print()
print('As pessoas com a idade acima da media ', end='')
print()
for idad in cadastro:
    if idad['idade'] >= media:
        print(f'Nome: {idad["nome"]} com {idad["idade"]} anos\n', end='')
print()
print(f'<<'*8, 'ENCERRANDO', '>>'*8)
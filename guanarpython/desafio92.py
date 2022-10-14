from datetime import date
cadastro = {}
cadastro['nome'] = input('Nome: ')
nasci = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - nasci
cadastro['sexo'] = input('Sexo: [F/M] ').upper()
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    if cadastro['sexo'] in 'Ff':
        cadastro['aposentadoria'] = (cadastro['contratação'] + 30) - nasci
    elif cadastro['sexo'] in 'Mm':
        cadastro['aposentadoria'] = ((cadastro['contratação'] + 35)) - nasci
print('-='*30)
for ke, val in cadastro.items():
    print(f'    - {ke} tem o valor {val}')

sex = input('Sexo [M/F}: ').strip().upper()[0]
while sex not in 'fFMm':
    sex = input('Dado Inválido, Digite seu sexo [M/F]:  ').strip().upper()[0]
print(f'Sexo {sex} cadastrado com sucesso')
print('Fim')

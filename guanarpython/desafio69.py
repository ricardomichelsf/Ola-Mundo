'''pes = 0
mas = 0
mul = 0
ida = int(input('Digite a idade: '))
sex = input('Sexo [M/F]: ').strip()[0]
while True:
    if sex in 'MmFf':
        if ida >= 18:
            pes += 1
        if sex in 'Mm':
            mas += 1
        if sex in 'Ff' and ida < 20:
            mul += 1
        opc = input('Quer continuar? [S/N]: ').strip()[0]
        if opc in 'Nn':
            break
        if opc in 'Ss':
            ida = int(input('Digite a idade: '))
            sex = input('Sexo [M/F]: ').strip()[0]
        else:
            opc = input('Quer continuar? [S/N]: ').strip()[0]
    else:
        sex = input('Sexo [M/F]: ').strip()[0]
print(f'{pes} tem mais 18 anos')
print(f'Foram cadastrados {mas} homens')
print(f'Tem {mul} mulher(s) menor(s) de 20 anos')'''
tot18 = totH = totM20 = 0
while True:
    ida = int(input('Idade: '))
    sex = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if ida >= 18:
        tot18 += 1
    if sex == 'M':
        totH += 1
    if sex == 'F' and ida < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [N/S] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos : {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos ')

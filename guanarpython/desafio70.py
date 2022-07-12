'''som = car = bar = cont = 0
con = 'S'
mai = ''
while True:
    while con in 'Ss':
        nom = input('Nome do produto: ')
        pre = float(input('Valor: '))
        con = input('Quer continuar [S/N] ').upper().strip()[0]
        som += pre
        cont += 1
        if pre > 1000:
            car += 1
        if cont == 1 and pre < bar:
            bar = pre
            mai = nom
    if con in 'Nn':
        break
    else:
        con = input('Quer continuar [S/N] ').upper().strip()[0]
print(f'O total gasto foi de R${som}')
print(f'Nessa compra há {car} produtos que custa mais de R$1000')
print(f'O produro mais barato é {mai} cústando R${bar})'''
tot = totmil = menor = cont = 0
barato =''
while True:
    produ = input('Nome do Produto: ')
    pre = float(input('Preço: '))
    cont += 1
    tot += pre
    if pre > 1000:
        totmil += 1
    if cont == 1 or pre < menor:
        menor = pre
        barato = produ
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
         break
print('{:-^40}'.format('Fim do Programa'))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

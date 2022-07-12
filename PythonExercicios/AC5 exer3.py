quantid = 1
maiorP = 0
encontrado = False

while quantid != 0:
    item = input().split(" ")

    cod = item[0]
    quantid = int(item[1])
    preco = float(item[2])

    preco_total = quantid * preco

    if preco_total > maiorP:
        codigo = cod
        quant = quantid
        preco_item = preco_total

        encontrado = True

if encontrado:
    print('Item mais caro')
    print(f'Codigo: {codigo}')
    print(f'Quantidade: {quant}')
    print('Custo: {:.2f}'.format(preco_item)
else:
    print('nao tem compras')
import math
area = float(input())
litros = area / 7
latas24 = math.ceil(litros / 24)
custo = 91 * latas24
saida1 = 'a) {} lata(s) de 24 litros: R$ {:2,.2f}'
print(saida1.format(latas24, custo))


latas5_4 = math.ceil(litros / 5.4)
custo = 23 * latas5_4
saida2 = 'b) {} lata(s) de 5.4 litros: R$ {:2,.2f}'
print(saida2.format(latas5_4, custo))

latas24 = math.floor(litros / 24)

litros = litros - (latas24 * 24)

latas5_4 = math.ceil(litros / 5.4)

total = (latas24 * 91) + (latas5_4 * 23)

saida = 'c) {} lata(s) de 24 litros e {} lata(s) de 5.4 litros: R$ {:2,.2f}'
print(saida.format(latas24, latas5_4, total))


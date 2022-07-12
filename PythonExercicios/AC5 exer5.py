"""def converte(ano2):
    convertida = []
    for i in ano2:
        convertida.append(int(i))
    return convertida

def valid(conv):
    ano2 = converte(conv)
    atual = 2020
    for x in ano2:
        if x < 1000:
            ano = print('Ano invalido')
        elif x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
            ano = print('O ano {} é BISSEXTO'.format(x))
        else:
            ano = print('O ano {} não é BISSEXTO'.format(x))
    return ano

ano1 = input().split(" ")
x = valid(ano1)
"""
def contaDigitos():
    posic = 0
    for ano_veri in anos:
        cont =len(anos[posic])
        posic += 1
        if cont == 4:
            bissexto(ano_veri)
        else: print("Ano invalido")

def bissexto(ano_veri):
    ano_ve = int(ano_veri)
    if ano_ve % 4 == 0 and ano_ve % 100 != 0 or ano_ve % 400 == 0:
        menssagem(ano_ve)
    else: print('O ano {} NAO eh bissexto'.format(ano_ve))

def menssagem(ano_ve):
    if ano_ve == 2020:
        print('O ano {} eh bissexto'.format(ano_ve))
    elif ano_ve <= 2000:
        print('O ano {} foi bissexto'.format(ano_ve))
    else:
        print('O ano {} serah bissexto'.format(ano_ve))

anos = input().split(" ")
contaDigitos()

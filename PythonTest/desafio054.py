from datetime import date
print('VOCÊ JÁ É MAIOR DE IDADE?')
co = 0
atu = date.today().year
con = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    if atu - ano >= 21:
        co = co + 1
    else:
        con = con + 1
print('{} pessoa(s) ainda não passaram da maioridade'.format(con))
print('Ao todo tivemos {} pessoas maiores de idade'.format(co))

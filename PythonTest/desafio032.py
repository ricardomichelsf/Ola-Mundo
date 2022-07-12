from datetime import date
ano = int(input('Digite o ano a ser analísado? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print("O ano \033[1;33;40m{} é Bissexto\033[m!!".format(ano))
else:
    print('O ano \033[1;33;40m{} não é Bissexto\033[m!!'.format(ano))
print(date.today())
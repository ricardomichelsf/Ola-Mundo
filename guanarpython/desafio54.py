from datetime import date
mai = 0
men = 0
ano = date.today().year
for c in range(1, 8):
    nas = int(input('Em que ano você nasceu: '))
    if ano - nas >= 21:
        mai += 1
    else:
        men += 1
print(f'Temos {mai} maiores de 21 e {men} menores')

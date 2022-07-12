inic = int(input('Digite em que númeroo irá começar: '))
raz = int(input('Razão: '))
term = inic
c = 1
while c <= 10:
    print(term, end=' -> ')
    term = term + raz
    c += 1
print('FIM')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'\033[1:30mO primeiro número {n1} é o maior número digitado\033[m')
elif n2 > n1:
    print(f'\033[1:30mO segundo número {n2} é o maior número digitado\033[m')
else:
    print('\033[1:30mNão existe valor maior os dois são iguais\033[m')

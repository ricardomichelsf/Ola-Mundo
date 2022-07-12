print('\033[7;30mQual o maior número?\033[m')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('\033[36mO primeiro número digitado {} é maior que {}\033[m'.format(n1,n2))
elif n2 > n1:
    print('\033[36mO segundo número digitado {} é maior que {}\033[m'.format(n2, n1))
else:
    print('\033[36mNão existe valor maior, os dois números {} e {} são iguais\033[m'.format(n1, n2))

num = 0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
while num != 5:
    print('''ESCOLHA O QUE FAZER
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS VALORES
    [ 5 ] SAIR''')
    num = int(input('qual você escolhe? '))
    if num == 1:
        som = n1 + n2
        print(f'A soma dos números {n1} e {n2} é {som}')
    elif num == 2:
        mul = n1 * n2
        print(f'A multiplicação é {mul}')
    elif num == 3:
        if n1 > n2:
            mai = n1
            print(f'O maior valor digitado foi {n1}')
        else:
            mai = n2
            print(f'O maior valor digitado foi{n2}')
    elif num == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite um valor: '))
    elif num > 5:
        print('Número invalido')
print('Fim do Programa')

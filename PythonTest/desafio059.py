'''sai = 5
esc = (0, 5)
while esc != sai:
    num = int(input('Digite um valor: '))
    num1 = int(input('Digite outro valor: '))
    print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa""")
    esc = int(input('Escolha qual a função você quer: '))
    if esc == 1:
        print('A soma desses números é {}'.format(num + num1))
    if esc == 2:
        print('O resultado desses valores é {}'.format(num * num1))
    if esc == 3:
        if num > num1:
            print('O maior número digitado foi {}'.format(num))
        else:
            print('O maior número digitado foi {}'.format(num1))
    if esc == 4:
        print('Digite outros números')
print('Fim')'''
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opçao = int(input('>>>>> Qual é a sua opção? '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opçao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamante')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa! Volte sempre!')


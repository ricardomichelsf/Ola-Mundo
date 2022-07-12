def contaDigitos():
    lista = (input().split(' '))
    x = 0
    for _ in lista:
        conta = len(lista[x])
        x += 1
        print(conta)
cont = 'S'
num = n2 = med = 0
while cont in 'Ss':
    n1 = int(input('Digite um número: '))
    num += 1
    if num == 1:
        mai = men = n1
    else:
        if n1 > mai:
            mai = n1
        if n1 < men:
            men = n1
    n2 += n1
    cont = input('Quer continuar [S/N]: ').upper().strip()[0]
med = n2 / num
print(f'A media dos valores é {med}')
print(f'O maior valor é {mai} e o menor valor é {men}')

num = int(input('Digite um nuúmero entre 0 e 9999: '))
uni = num % 10
dez = num // 10 % 10
mil = num // 1000 % 10
cen = num // 100 % 10
print(f'a unidade é {uni}')
print(f'A dezena é {dez:.0f}')
print(f'A centena é {cen}')
print(f'A milhar é {mil}')

'''nu1 = input('Digite um número entre 0 e 9999: ')
print(f'Unidade {nu1[3]}')
print(f'A dezena é {nu1[2]}')
print(f'A centena é {nu1[1]}')
print(f'A milhar é {nu1[0]}')'''

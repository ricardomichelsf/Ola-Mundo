num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitado forma ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

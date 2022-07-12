n1 = int(input('\033[36mDigite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número:\033[m'))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('\033[32mO menor número é: {}'.format(menor))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número é: {}\033[m'.format(maior))
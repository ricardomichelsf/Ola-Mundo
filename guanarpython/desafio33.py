n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Diite outro número: '))
'''if n1 > n2 and n1 > n3:
    maior = n1
    print(f'O maior número digitado foi {maior}')
elif n2 > n3 and n2 > n1:
    maior = n2
    print(f'O maior número digitado foi {maior}')
else:
    maior = n3
    print(f'O maior número digitado foi {maior}')
if n1 < n2 and n1 < n3:
    menor = n1
    print(f'O menor número digitado foi {menor}')
elif n2 < n1 and n2 < n3:
    menor = n2
    print(f'O menor número digitado foi {menor}')
else:
    menor = n3
    print(f'O menor número dogitado foi {menor}')'''
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n1:
    maior = n3
print(f'O número mairo é {maior}')
print(f'O número menor é {menor}')

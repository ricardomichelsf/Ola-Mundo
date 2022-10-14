'''num = int(input('Digite um número: '))
cont = num
while cont > 1:
    cont -= 1
    num *= cont
print(f'fatorial é {num}')
'''
from math import factorial
num = int(input("Digite um número: "))
f = factorial(num)
print(f"O fatorial de {num} é {f}")

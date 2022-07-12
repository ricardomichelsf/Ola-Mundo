r = int(input())
pa = int(input())
soma = 1
total = 1
while soma < pa:
    soma += r
    total += soma
print(f'A somatoria da PA eh: {total}')

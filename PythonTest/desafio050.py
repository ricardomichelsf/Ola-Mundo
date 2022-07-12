s = 0
for c in range(1, 7):
    n = int(input('Digite {} número: '.format(c)))
    if n % 2 ==0:
        s += n
print('A soma dos numeros pares é {}'.format(s))
print('fim')

''' fra = input('Digite uma frase: ').strip().upper()
fr = (''.join(fra.split()))
f1 = fr[::-1]
print(f'O invrso de {fr} é {f1}')
if fr == f1:
    print(f'A frase {fra} é um palindromo')
else:
    print(f'A frase {fra} não é um palindromo') '''

fra = input('Digite uma frase: ').strip().upper()
fr = (''.join(fra.split()))
inver = ''
for letra in range(len(fr) - 1, - 1, - 1):
    inver += fr[letra]
print(f'O invrso de {fr} é {inver}')
if fr == inver:
    print(f'A frase {fra} é um palindromo')
else:
    print(f'A frase {fra} não é um palindromo')

'''num = int(input('Digite um número: '))
co = 1
fi = 1
seq = 0
print('~~'*20)
while co <= num:
    print(seq, end=' -> ')
    fi = fi + seq
    seq = fi - seq
    co += 1
print('Fim')
print('~~'*20)'''

n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end=' -> ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')

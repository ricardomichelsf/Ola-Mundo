'''n = 1
while True:
    print('=' * 35)
    num = int(input('Quer ver a tabuada de qual valor? '))
    while n <= 10:
        print(f'{num} X {n:2} = {num * n}')
        n += 1
        if n > 10:
            n = 1
            print('=' * 35)
            num = int(input('Quer ver a tabuada de qual valor? '))
        elif num < 0:
            break
    else:
        break
print('\033[1mPrograma tabuada encerrado Volte sempre\033[m')'''
while True:
    n = int(input('Quer ver a tabuada do? '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')
    print('-'*30)
print('Volte sempre')

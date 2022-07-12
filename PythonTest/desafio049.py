print('\033[7;30mTABUADA\033[m')
n = int(input('Digite qual a tabuada você quer: '))
for c in range(0, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))

num = int(input('\033[31mDigite o número:\033[m '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[32mAnalisando o número {}\033[m'.format(num))
print('\033[33mUnidade: {}\033[m'.format(u))
print('\033[34mDezena: {}\033[m'.format(d))
print('\033[35mCentena: {}\033[m'.format(c))
print('\033[36mMilhar: {}\033[m'.format(m))


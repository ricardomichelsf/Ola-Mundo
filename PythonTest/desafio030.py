num = int(input('\033[33mDigite um número:\033[m '))
res = num % 2
if res == 0:
    print('\033[36mO número {} é PAR!\033[m'.format(num))
else:
    print('\033[32mO número {} é IMPAR!\033[m'.format(num))
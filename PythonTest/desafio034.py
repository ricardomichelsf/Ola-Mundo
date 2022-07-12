sal = float(input("Digite o seu salário: "))
sup = sal + (sal * 10/100)
inf = sal + (sal * 15/100)
if sal >= 1250:
    print('Seu novo salário é \033[7;30m{:.2f}\033[m'.format(sup))
else:
    print('Seu novo salário é \033[36m{:.2f}\033[m'.format(inf))
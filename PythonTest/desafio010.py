n1 = float(input('\033[1;7;30mQuanto você tem em dinheiro: R$ \033[m'))
print('Você tem R$ {} em reais \nPode comprar $ \033[1;7;30m{:.2f}\033[m dólares'.format(n1, n1/3.20204))
print('Você pode comprar $ \033[1;36m{:.2f}\33[m euros'.format(n1/3.85))

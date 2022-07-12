pre = float(input('\033[1;7;30mDigite o valor do produto :\033[m '))
des = pre * 0.05
print('O valor do produto é {} reais, mas com o desconto de 5% ele fica {:.2f} reais'.format(pre, pre-des))

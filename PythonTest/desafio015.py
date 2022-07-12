d = float(input('\033[31mQuantos dias o carro ficou alugado: '))
km = float(input('Quantos km foram rodados:\033[m '))
al = d * 60
rd = km * 0.15
print('\033[36mO valor total a ser pago é de R${:.2f}\033[m'.format(al + rd))
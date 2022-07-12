print('\033[7;30mCalcúle o valpor a ser pago\033[m')
pre = float(input('Digite o valor do produto: '))
print('Escolha a forma de pagamento?')
esc = int(input('''[1] À vísta digite
[2] À vista no cartão digite
[3] 2x no cartâo digite
[4] 3x ou mais no cartão digite 
A opção digitada é: '''))
if esc == 1:
    print('Você escolheu pagar à vista e pagará {}'.format(pre - (pre * 0.1)))
elif esc == 2:
    print('Você escolheu pagar à vista no cartão e pagará {}'.format(pre - (pre * 0.05)))
elif esc == 3:
        print('Você escolheu pagar 2x no cartão e pagará {}'.format(pre))
elif esc ==4:
    par = int(input('Quantas parcelas? '))
    acre = pre + (pre * 0.2)
    print('Você escolheu pagar {}x de R${} no cartão\nsua compra sairá por {}'.format(par, (acre / par), acre))
else:
    pre = 0
    print('Opção Inválida tente novamente')


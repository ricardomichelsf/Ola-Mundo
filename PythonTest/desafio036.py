print('\033[1;4;36mEmpréstimo bancário para a compra de uma casa\033[m')
cas = float(input('\033[32mDigite o valor da casa: '))
sal = float(input('Digite o seu salário R$: '))
ano = int(input('Em quantos anos você pretende pagar:\033[m '))
par = ano * 12
val = cas / par
exc = sal * 0.3
if val <= exc:
    print('\033[36mPARABÉNS SEU EMPRÉSTIMO FOI APROVADO')
    print('Você pagara {} reais em {} anos '.format(cas, ano))
    print('Por mês você pagará R${:.2f} reais \033[m'.format(val, ano))
else:
    print('\033[31mDesculpe mas infelizmente você não poderá financiar essa casa')
    print('A parcela de {:.2f} reais ultrapassa 30% do seu salario que é {:.2f}\033[m'.format(val,exc))

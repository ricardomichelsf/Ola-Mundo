print('   \033[7:30mAPROVAÇÃO DE EMPRÉTIMO\033[m')
print('='*28)
casa = float(input('Digite o valor da casa R$ '))
sal = float(input('Digite o seu salário R$ '))
ano = int(input('Quantos anos para pagar: '))
qnt = ano * 12
sala = sal * 0.3
emp = casa / qnt
print(f'O valor das parcelas ficaram em R${emp:.2f}')
if emp > sala:
    print('Seu empréstimo foi \033[1:35mNEGADO\033[m pois passa de 30% do salário')
else:
    print('\033[1:35mPARABÉNS!!!\033[m Seu empréstimo foi aprovado')


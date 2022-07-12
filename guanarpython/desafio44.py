pre = float(input('Digite o preço do produto R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartâo''')
form = int(input('Qual a opção? '))
if form == 1:
    pre = pre -(pre * 0.1)
    print(f'Seu produto irá ficar por R${pre} reais')
elif form == 2:
    pre = pre -(pre * 0.05)
    print(f'Seu produto irá ficar R${pre} reais')
elif form == 3:
    pre = pre / 2
    print(f'Você irá pagar R$ {pre} reais por parcela')
elif form == 4:
    vez = int(input('Quantas vezes no cartão? '))
    jur = ((pre * 0.20) + pre)
    par = jur / vez
    print(f'Você irá pagar {vez}x de R$ {par} reais com juros')
    print(f'Sua compra de R${pre:.2f} vai custar {jur:.2f} no final ')
else:
    print('\33[1:31m OPÇÃO INVÁLIDA!!')



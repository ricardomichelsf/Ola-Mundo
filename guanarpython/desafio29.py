km = int(input('Digite a velocidade do um carro: '))
if km > 80:
    mul = (km - 80) * 7
    print(f'Você foi multado e ira pagar R$ {mul:.2f}')
else:
    print('Você está dentro do limite')

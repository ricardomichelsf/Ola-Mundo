dia = int(input('Quantos dias o carros foi alugado? '))
km = float(input('Quantos Km rodados? '))
alu = dia * 60
rod = km * 0.15
print(f'O total a pagar é de R$ {alu + rod}')

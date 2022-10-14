gastos = [15.00, 57.50, 83.25, 11.75, 2.0, 52.50, 97.75, 72.25]
essencial = [True, False, False, True, True, True, False, True]

gastos_essenciais = 0
gastos_nao_essenciais = 0

for gasto in range(len(gastos)):
    if essencial[gasto]:
        gastos_essenciais += gastos[gasto]
    else:
        gastos_nao_essenciais += gastos[gasto]

print(f'Gastos essenciais R$ {gastos_essenciais}')
print(f'Gasto Não essenciais R$ {gastos_nao_essenciais}')


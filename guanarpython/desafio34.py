sal = float(input('Digite o salário para saber o aumento R$ '))
if sal >= 1250:
    nov = (sal * 0.1) + sal
    print(f'Seu novo salário é de R$ {nov:.2f}')
else:
    nov = (sal * 0.15) + sal
    print(f'Seu novo salário é de R$ {nov:.2f}')

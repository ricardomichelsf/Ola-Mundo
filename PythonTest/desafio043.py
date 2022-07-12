print('\033[36mCalcule o IMC\033[m')
peso = float(input('Digite o seu peso: '))
alt = float(input('Digite a sua altura: '))
imc = peso /(alt ** 2)
if imc <= 18.5:
    print('Você está abaixo do peso seu indice de IMC é {:.2f}'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Você esta no peso ideal seu indice de IMC é {:.2f}'.format(imc))
elif imc > 25 and imc < 30:
    print('Você está com sobrepeso seu indice de IMC é {:.2f}'.format(imc))
elif imc > 30 and imc < 40:
    print('Você está com obesidade seu indice de IMC é {:.2f}'.format(imc))
elif imc > 40:
    print('Você está com obesidade mórbida seu indice de IMC é {:.2f}'.format(imc))

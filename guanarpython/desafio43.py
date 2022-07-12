alt = float(input('Digite a sua altura: '))
pes = float(input('Digite o seu peso: '))
imc = pes/(alt ** 2)
print(f'O IMC dessa pessoa é {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está de sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Morbida')

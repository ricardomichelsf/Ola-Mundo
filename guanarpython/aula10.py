nome = input('Qual é o seu nome: ').strip().upper()
if nome == 'RICARDO':
    print(f'Que lindo nome você tem !!')
else:
    print('Seu nome é tão normal')
print(f'Boa noite, {nome}')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa! Parabens!')
else:
    print('A sua média foi ruim estude mais')


escola = {}
escola['nome'] = input('Nome: ')
escola['nota'] = []

for se in range(1,5):
    nota = float(input(f'Digite a {se}° nota: '))
    escola['nota'].append(nota)

escola['media'] = (sum(escola['nota'])) / len(escola['nota'])
if escola['media'] >= 7:
    escola['situação'] ='Aprovado'
elif 5 <= escola['media'] > 7:
    escola['situação'] = 'Recuperação'
else:
    escola['situação'] = 'Reprovado'

print(f'{escola["nome"]} sua média doi de {escola["media"]} você está {escola["situação"]}')

resp = input("Gostaria de ver suas notas? [S/N] ").upper()

if resp in 'Ss':
    print(escola['nota'])
    print("Fim")
else:
    print("Fim")


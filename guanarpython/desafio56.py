idade = 0
hom = ''
mai = 0
mulh = 0
for c in range(1, 5):
    print(f'---- {c}° PESSOA ----')
    nom = input('Nome: ').strip().upper()
    ida = int(input('Idade: '))
    sex = input('Sexo [M/F]: ').strip().upper()
    idade += ida
    med = (idade) / 4
    if ida > mai and sex == 'M':
        mai = ida
        nome = nom
    elif ida < 20 and sex == 'F':
        mul = 1
        mulh = mulh + mul
print(f'A média de idade do grupo é {med}')
print(f'O homem mais velho tem {mai} seu nome é {nome}')
print(f'Ao total tem {mulh} mulheres menores de 20 anos')


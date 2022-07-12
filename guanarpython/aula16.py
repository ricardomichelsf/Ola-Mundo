lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posiçãa {pos}')
print('Comi pra caramba')
print(sorted(lanche))
print(lanche)

a = (2, 5, 4)

b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(2))

pessoa = ('Ricardo', 32, 'M', 132.35)
del(pessoa)#Deletando tupla inteira
print(pessoa)

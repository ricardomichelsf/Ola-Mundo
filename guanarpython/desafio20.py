from random import shuffle
alu1 = input('DIgite um nome: ')
alu2 = input('Digite um nome: ')
alu3 = input('Digite um nome: ')
alu4 = input('Digite um nome: ')
lis = [alu1, alu2, alu3, alu4]
shuffle(lis)
print(f'A ordem de apresentação ficou {lis}')

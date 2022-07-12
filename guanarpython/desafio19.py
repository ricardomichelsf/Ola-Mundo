from random import choice
alu1 = input('Digite um nome: ')
alu2 = input('Digite um nome: ')
alu3 = input('Digite um nome: ')
alu4 = input('Digite um nome: ')
lis = [alu1, alu2, alu3, alu4]
esco = choice(lis)
print(f'O aluno escolhido para limpar o quadro foi {esco}')

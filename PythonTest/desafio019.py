import random
a1 = input('\033[36mDigite o nome do Aluno: ')
a2 = input('Digite o nome do Aluno: ')
a3 = input('Digite o nome do Aluno: ')
a4 = input('Digite o nome do Aluno: \033[m')
al = (a1, a2, a3, a4)
print('{}'.format(al))
print('\033[32mO Aluno escolhido foi {}\033[m'.format(random.choice(al)))


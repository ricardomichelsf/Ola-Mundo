import random
a1 = str(input("Qual o nome do aluno1: "))
a2 = str(input('Qual o nome do aluno2: '))
a3 = str(input('Qual o nome do aluno3: '))
a4 = str(input('Qual o nome dp aluno4: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('\033[1;36mA ordem de apresentação é:\033[m')
print(lista)
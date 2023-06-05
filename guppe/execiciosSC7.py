"""
Exercicio 1
vetor =[1, 0, 5, -2, -5, 7]
soma = 0
for indice, num, in enumerate(vetor):
    if indice == 0 or indice == 1 or indice == 5:
        soma += num
print(soma)
vetor[4] = 100

Exercicio 2
for num in vetor:
    print(num)

Exercicio 3
lista = [2, 3, 5, 4, 7, 9, 10, 8, 6, 11]
quadr = []
for n in lista:
    n = n ** 2
    quadr.append(n)

print(*lista)
print(*quadr)

Exercicio 4
vetor = [8, 9, 45, 21, 36, 12, 30, 51]
num1 = int(input('Digite uma posição de 1 a 8: '))
num2 = int(input('Digite uma posição de 1 á 8: '))

soma = vetor[num1] + vetor[num2]

print(f'A soma dos valores encontrdos nas posições {num1} e {num2} é {soma}')

Exercicio 5
vetor = [8, 9, 45, 21, 36, 12, 30, 51]
par = 0
for pa in vetor:
    if pa % 2 == 0:
        print(pa, end=", ")
        par += 1

print(f'\nNo total tem {par} números pares')

Exercicios 6
vetor = []
for nu in range(0, 10):
    posi = int(input('Digite 10 valores e o sistema mostrará o maior e o menor: '))
    vetor.append(posi)

print(f"O maior número digitado foi {max(vetor)} e o menor {min(vetor)} os números digitados foram {vetor} ")

Exercicio 7
vetor = []
for nu in range(0, 5):
    posi = int(input('Digite 10 valores e o sistema mostrará o maior e posicao: '))
    vetor.append(posi)

print(f'O maior numero foi {max(vetor)} e esta na posição {vetor.index(max(vetor))}\n.', *vetor)

Exercicio 8 
vetor = []
for nu in range(0, 6):
    posi = int(input('Digite 6 valores: '))
    vetor.append(posi)
print(*vetor)
vetor.reverse()
print(f'\nMostrarei os valores na forma inversa {vetor}')

Exercicio 9
vetor = []
qtd = 0
while qtd < 6:
    num = int(input('Digite um número par: '))
    if num % 2 == 0:
        vetor.append(num)
        qtd += 1

vetor.reverse()
print(vetor)

Exercicio 10

notas = []
print('Digite 15 notas de alunos')
for n1 in range(0, 15):
    nota = float(input('Digite a nota:'))
    notas.append(nota)

print(f'A média geral da classe é {sum(notas)/len(notas):.2f}')

Exercicio 11


"""


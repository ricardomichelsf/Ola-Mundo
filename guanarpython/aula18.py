"""test = []
test.append('Gustavo')
test.append(40)
galera = list()
galera.append(test[:])
test[0] = 'Maria'
test[1] = 22
galera.append(test[:])
print(galera)
galera = [['João', 19],['Ana', 33],['Maria', 45],['Joaquim', 13]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')"""
 
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
        totmai += 1
    
    else:
        print(f'{pessoa[0]} é menor de idade')
        totmen += 1

print(f'O total de pessoas maior de 21 é {totmai} e menor de 21 é {totmen}')
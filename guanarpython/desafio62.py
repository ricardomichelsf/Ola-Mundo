pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
ter = 10
co = 1
som = pri
while co <= ter:
    print(som, end=' -> ')
    som = som + raz
    if co == ter:
        mos = int(input("\nQuantos termos vc quer mostra mais? "))
        ter += mos
    co += 1
print(f'Progressão finalizada você mostrou {ter} termos')

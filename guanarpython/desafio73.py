def lin():
    print('==='*40)

tab = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético - MG',
        'Athletico Paranaense', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense',
        'Corinthians','Chapecoense', 'Ceará', 'Vasco da Gama', 'America','Sport', 'Vitória',
        'Paraná')

lin()
print(f'Lista de Times do Brasileirão: {tab}')
lin()
print(f'Os 5 primeiros colocados são: {tab[:5]}')
lin()
print(f'Os 4 últimos são: {tab[-4:]}')
lin()
print(f'Times em ordem alfabética: {sorted(tab)}')
lin()
print(f'Chapecoense está na {tab.index("Chapecoense")+1}° posição')
lin()

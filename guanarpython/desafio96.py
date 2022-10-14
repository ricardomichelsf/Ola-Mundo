def controTerreno(lar, comp):
    total = lar * comp
    print(f'A área de um terreno {lar}x{comp} é de {total}m².')


print('Controle de Terrenos')
print('-'*20)
largu = float(input('LARGURA(m): '))
compri = float(input('COMPRIMENTO (m): '))
controTerreno(largu, compri)

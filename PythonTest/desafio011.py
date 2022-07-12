lar = float(input('\033[1;36mDigite a largura da parede:\033[m '))
alt = float(input('\033[1;34mDigite a altura da parede:\033[m '))
area = lar * alt
print('Essa parede tem {:0.2f} m² e gastará {:0.2f} litros de tinta'.format(area, area/2))
import math
ca = float(input('\033[1;36mDigite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))
hi = math.hypot(ca, co)
print('\033[mA hipotenesa é {:.2f}'.format(hi))

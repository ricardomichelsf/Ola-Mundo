print('\033[7;30mDigite o comprimento de 3 retas ?\033[m')
r1 = float(input('Primeira: '))
r2 = float(input('Segunda: '))
r3 = float(input('Terceira: '))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;4;34mSim ele é um triângulo!\033[m')
else:
    print('\033[1;4;36mEstas retas não formam um triângulo!\033[m')


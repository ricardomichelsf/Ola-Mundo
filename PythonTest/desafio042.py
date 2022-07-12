print('\033[34mMostre se estás retas formam um triângulo e qual triângulo?\033[m')
r1 = float(input('\033[36mDigite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[36mSim elas formam um triângulo\033[m')
    if r1 == r2 == r3:
        print('Este é um triângulo Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Este é um triângulo Escaleno')
    else:
        print('Este é um triângulo Isósceles')
else:
    print('Estás retas não formam um triângulo')

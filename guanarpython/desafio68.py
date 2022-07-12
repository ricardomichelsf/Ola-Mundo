'''from random import randint
vit = 0
while True:
    print('='*26)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('='*26)
   # print("""    [ 1 ] IMPAR
    [ 2 ] PAR """)
    esco = int(input('Qual você escolhe: '))
    if esco == 1 or esco == 2:
        num = int(input('Digite um número: '))
        lis = randint(0,10)
        print('=' * 26)
        print(f'Computador escolheu {lis}')
        veri = num + lis
        print(f'A soma desses valores foi {veri}')
        if esco == 2 and veri % 2 == 0 or esco == 1 and veri % 2 != 0:
            if esco == 1:
                print('Voce escolheu IMPAR')
            else:
                print('Você escolheu PAR')
            print('GANHOU')
            vit += 1
        elif esco == 2 and veri % 2 != 0 or esco == 1 and veri % 2 == 0:
            if esco == 1:
                print('Voce escolheu IMPAR')
            else:
                print('Você escolheu PAR')
            print('PERDEU')
            break
    else:
        print('=' * 26)
        print('OPÇÃO IUNVÁLIDA, TENTE NOVAMENTE')
print('='*26)
print(f'Você ganhou {vit} vezes')'''
from random import randint
v = 0
while True:
    joga = int(input('Diga o valor: '))
    compu = randint(0,10)
    total = joga + compu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? {P/I] ')).strip().upper()[0]
    print(f'Você jogou {joga} e o computador {compu} . total de {total}')
    print('Deu Par' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar de novo...')
print(f'Você venceu {v} vezes')


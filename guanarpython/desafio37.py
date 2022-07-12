num = int(input('Digite um numero: '))
print('ESCOLHA EM QUE FORMA VOCÊ QUER CONVERTER')
print('1 - BINáRIO ')
print('2 - OCTALDECIMAL')
print('3 - HEXADECIMAL')
esco = int(input('Qual você escolhe: '))
if esco == 1:
    print('Em binario fica {}'.format(bin(num)[2:]))
elif esco == 2:
    oc = oct(num)
    print(f'Em OCTAL fica {oc[2:]}')
elif esco == 3:
    hes = hex(num)
    print(f'Em HEXA fica {hes[2:]}')

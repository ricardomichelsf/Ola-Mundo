from datetime import date
print('\033[31mAlistamento já está na hora?\033[m')
sex = str(input('Digite o seu sexo f ou m: '))
nas = int(input('\033[36mDigite o ano de nascimento:\033[m '))
atu = date.today().year
res = atu - nas
fal = 18 - res
pas = res - 18
print('\033[36mQuem nasceu em {} tem {} anos em {}\033[m'.format(nas, res, atu))
if sex == 'f':
    print ('\033[7;30mVocê não precisa se alista\033[m')
elif res < 18:
    print('\033[36mAinda falta {} anos para você se alistar'.format(fal))
    ano = atu - fal
    print('Seu alistamento será em {}\033[m'.format(ano))
elif res == 18:
    print('\033[36mJá está na hora de se alistar\033[m')
else:
    print('\033[36mJá passou {} anos que você deveria ter se alistado'.format(pas))
    ano = atu - pas
    print('Seu alistamento foi em {}\033[m'.format(ano))


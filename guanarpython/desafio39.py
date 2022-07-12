from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
sex = input('Sexo M/F: ').strip().upper()
atu = date.today().year
alis = atu - ano
ida = 18 - alis
tem = ano + 18
if sex == 'M':
    if alis == 18:
        print(f'\033[1:30m Esse ano você faz {alis} anos já está na hora de se alistar ')
    elif alis < 18:
        print(f'Falta {ida} anos para você se alistar')
        print(f'Você irá se alistar em {tem}')
    else:
        print(f'Você está {ida *(-1) } anos atrasado para se alista ')
        print(f'Seu alistamento foi em {tem}')
elif sex == 'F':
    print('Você é Mulher não precisa se allistar')
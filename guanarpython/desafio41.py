from datetime import date

ano = int(input('Digite o ano do nascimento: '))
atu = date.today().year
ida = atu - ano
if ida <= 9:
    print(f'Com {ida} você está na categoria \033[1:30mMIRIM\033[m')
elif ida <=14:
    print(f'Com {ida} você está na categoria \033[1:30mINFANTIL\033[m')
elif ida <= 19:
    print(f'Com {ida} você está na categoria \033[1:30mJUNIOR\033[m')
elif ida <= 25:
    print(f'Com {ida} você está na categoria \033[1:30mSÊNIOR\033[m')
else:
    print(f'Com {ida} você está na categoria \033[1:30mMASTER\033[m')

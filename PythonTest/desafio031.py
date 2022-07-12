cal = float(input('\033[7;30mQual é a distância de sua viagem:\033[m '))
per = cal * 0.5
lon = cal * 0.45
if cal <= 200:
    print('\033[34mSua passagem custará: {:.2f} reais\033[m '.format(per))
else:
    print("\033[33mSua passsagem custará: {:.2f} reais\033[m ".format(lon))


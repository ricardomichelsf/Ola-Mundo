print('\033[7;30mCalcular da Média\033[m')
not1 = float(input("\033[36mDigite a primeira nota: "))
not2 = float(input('Digite a segunda nota:\033[m '))
med = (not1 + not2) / 2
if med < 5:
    print('\033[34mVocê foi REPROVADO sua média foi {:.1f}\033[m'.format(med))
elif 7 > med >= 5:
    print('\033[34mVocê ficou de RECUPERAÇÃO sua média foi {:.1f}\033[m'.format(med))
else:
    print('\033[34mPARABÉNS VOCÊ FOI APROVADO')
    print('Sua média foi {:.1f}\033[m'.format(med))

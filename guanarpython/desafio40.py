no1 = float(input('Digite a nota: '))
no2 = float(input('Digite outra nota: '))
med = (no1 + no2)/2
if med < 5:
    print(f'Sua média foi {med:.1f} você foi \033[1:36mREPROVADO\033[m estude mais ')
elif 7 > med >= 5:
    print(f'Sua média foi {med:.1f} você ficou de \033[1:34mRECUPERAÇÃO\033[m')
else:
    print(f'Sua média foi de {med:.1f} você foi \033[1:32mAPROVADO !!!\033[m')

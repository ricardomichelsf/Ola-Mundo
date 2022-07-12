sal = float(input('\033[35mDigite o salário:\033[m '))
au = sal * 0.15
print('\033[1;36mO seu salário antigo era R$ {} reais, \nSeu novo salário é R$ {:.2f} reais\033[m'.format(sal, sal+au))

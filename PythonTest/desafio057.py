"""con = 'S'
while con == 'S':
     sexo = str(input('\033[1;33mSexo [M,F]: ')).strip().upper()[0]
     if sexo != 'F' and sexo != 'M':
         print('Você digitou errado tente novamente!!')
     con = str(input('Você quer continuar [S, N]: ')).upper()
print('Sexo {} registrdo com sucesso'.format(sexo))
print('Fim\033[m')"""
sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

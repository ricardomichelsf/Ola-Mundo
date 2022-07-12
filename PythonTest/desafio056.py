somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('---- {}° PESSOA ----'.format(p))
    nom = str(input('Nome: ')).strip()
    ida = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip()
    somaidade += ida
    if p == 1 and sex in 'Mm':
        maioridadehomem = ida
        nomevelhov = nom
    if sex in 'Mm' and ida > maioridadehomem:
        maioridadehomem = ida
        nomevelho = nom
    if sex in 'Ff' and ida < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A idade média do grupo é {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
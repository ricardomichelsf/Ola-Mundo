from datetime import date
print('\033[33mConfederação Nacional de Natação')
print('Classificação de categorias de atletas\033[m')
ano = int(input('Digite o Ano de seu nascimento: '))
atual = date.today().year
cla = atual - ano
if cla <= 9:
    print('Você tem {} anos e está na categoria \033[36mMIRIM\033[m'.format(cla))
elif 14 >= cla > 9:
    print('Você tem {} anos e está na categoria \033[36mINFANTIL\033[m'.format(cla))
elif cla <= 19:
    print('Você tem {} anos e está na categoria \033[36mJUNIOR\033[m'.format(cla))
elif cla <= 25:
    print('Você tem {} anos e está na categoria \033[36mSÊNIOR\033[m'.format(cla))
else:
    print('Você tem {} anos e está na categoria \033[36mMASTER\033[m'.format(cla))

#\033[0:33:44m
"""STyle; 0 none - 1 bold - 4 underline - 7 negative
text cor: 30 branco - 31 vermelho - 32 verde - 33 amarela - 34 azul - 35 roxo - 36 azul bebe -
37 cinza.
back cor: 40 branco - 41 vermelho - 42 verde - 43 amarela - 44 azul - 45 roxo - 46 azul bebe -
47 cinza.
color rise"""
print('\033[7:33:44mOlá Mundo!\033[m')
'''a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')'''
nome = 'Ricardo'
print(f'Olá muito prazer em te conhecer, \033[4:34m{nome}\033[m !! ')
nome = 'Ricardo'
cores = {'Limpa': '\033[m]',
         'azul':'\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m'}
print(f"Olá muito prazer em te conhecer {cores['pretoebranco']} {nome}{cores['Limpa']}!!!")


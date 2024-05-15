"""
**kwargs

Poderiamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwagrs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizemos parÂmetros nomeados, e trasdorma esses parâmetros extras em um dicionário.

Exemplo

def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor preferida da {pessoa.title()} é {cor.title()}.')

cores(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

#OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores()
cores(geek='navy')

Excemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek!'
    return 'Não tenho certeza quem você é ...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='ESpecial'))

# Nas nossas funções podemos ter (Nesta ordem):
- ParÂmetros obrigatórios:
- *args
- Parâmetros default (não obrigarórios)
- **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'julia')
minha_funcao(4, 'vanessa', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Enetenda por quê é importante mater a ordem dos parâmetros na declaração

# Função na ordem correta de parâmetros
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


# Função na ordem incorreta de parâmetros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

'''
a = 1
b = 2
args = (3, )
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}
'''
print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Desempacotar com **kwargs

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nome(**nomes))

"""
def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict (a=1, b=2, c=3)

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
# OBS: Os nomes da chave em um dicionario devem ser o mesmodos parâmetros da função
soma_multiplos_numeros(**dicionario)



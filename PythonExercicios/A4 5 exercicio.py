sequencia = input()
x = input()

if sequencia.count(x) == 0:
    print('Caractere nao encontrado.')
else:
    print('O caractere buscado ocorre {} vezes na sequencia.'.format(sequencia.count(x)))
"""
s = input()
carac = input()

def contaCaractere(s, carac):
    c = 0
    for str in s:
        if(str == carac):
            c += 1
    return c

retorno = contaCaractere(s, carac)
if(retorno == 0):
    print('Caractere nao encontrado.')
else:
    print(f'O caractere buscado ocorre {retorno} vezes na sequencia.')
"""
"""
import collections

def cont_ocorrencias (a,b):
    numeros = str(a)
    repetidos = collections.Counter(numeros)
    return repetidos[b]

a = input()
b = input()
y = str(a)

for caracter in y:
    cont_ocorrencias (a,b)

if cont_ocorrencias (a,b) == 0:
    print("Caractere nao encontrado.")
else:
    print("O caractere buscado ocorre {} vezes na sequencia.". format(cont_ocorrencias (a,b)))
"""
"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas especificas:
- Pode ou não receber entradas de dados e retornar saida de daos:
-Muito úteis para executar procedimentos similares por repetidas vezes:

OBS: Se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada.

Exemplo de urtilização de funções:

DRY - Don't Repeat Yourself - Não repeta você mesmo / Não repita seu código

Protocolo senac dia 03/05/2024: 4633384


cores = ['verde', 'amarelo', 'azul', 'branco']
cores.append('Roxo')
# Utilizando a função integrada (built-in) do python print()
print(cores)
cores.clear()
print(cores)

Mas então, como definir funções?

Em Python, a forma de definir uma função é:
def nome_da_funcao(parametros):
    bloco_da_função

Onde: 
nome_da_função -> SEMRPRE, com letras minúsculas, e se for nome composto, separado por underline.
parametros -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não.
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo uma função
Também abrimos o bloco de código com ojá conhecido dois pontos : que é utilizado em Python para definir blocos

Definido a primeira função

def diz_oi():
    print('Oi!')

Obs: 
1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que essa função não recebe nenhumm paramentro de entrada
3 - Veja que esta função não retorna nada;

def cantar_parabens():
    print("Parabéns pra você")
    print('Nesta data querida')
    print('Muitas felicidades')

    
for n in range(5):
    cantar_parabens()

Em Python, podemos inclusive criar variáveis do tipo de uma funçãoe executar esta função através de variável

canta = canta_parabens

canta()

Funções com retorno

numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop : {ret_pop}')

OBS: Em Python, qunado uma função não rertorna nenhum valor, o retorno é None

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return

def quadrado_de_7():
    retrun 7 * 7

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

def outra_funcao():
    rerturn 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

from random import random

def sorteia_valores():
    # gera um número randomico entre 0 e 1
    valore = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(sorteia_valores())


# Funções com Parâmetros (de entrada)

- Funções que recebem dados para serem processadas dentro da mesma;
Se a gente pensar em um programa qualquer, geralmentemtemos;
entrada -> processamwento -> saida

Se a gente pensar em uma função, já sabemos que temos funções que;
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

def quadrado(numero):
    return numero * numero

print(quadrado(7))

Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada em uma função
quantos parâmetros forem necessaríos. Eles são separados por vírgulas.

Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelica', 'Jolie'))

A diferença entre Parâmetros e Argumentos

Parâmetros são variaveís declaradas na definição de uma função;
Argumentos são dados passados durante a execução de uma função;

A ordem do parâmetros importa;

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

Argumentos nomerados (Keywords Arguments)

Caso utilizarmos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome= nome, sobrenome= sobrenome))
print(nome_completo(sobrenome='Marques', nome= 'Marcia'))

"""

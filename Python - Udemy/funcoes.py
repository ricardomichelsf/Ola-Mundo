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

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo
"""
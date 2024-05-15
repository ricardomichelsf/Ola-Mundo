"""
Entendendo o *args

O args é parâmetro, como outro qualquer, Isso significa que você poderá
chamar de qualquer coisa , desde que comece com asteristico.

Exemplo:
*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args?

O parâmtreo *args utilizando em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutaveis.

Exemplo:

def soma_todos(*args):
    return sum(args)

print(soma_todos('angelina', 'jolie', 3, 2, ))
print(soma_todos('angelina', 'jolie', 3, 2, 4))
print(soma_todos('angelina', 'jolie', 3.5, 7.2, 4))

#Outro exemplo usando *args

def verifica_informacao(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem você é!'

print(verifica_informacao())
print(verifica_informacao(1, True, 'University', 'Geek'))
print(verifica_informacao(1, 'University', 3.145))

"""
def soma_todos(*args):
    return sum(args)

numeros = [2, 1, 3, 4, 5, 7]
# Desempacotador
print(soma_todos(*numeros))

#OBS: O asteristico serve para que informemos ao Python que estamos 
#passando como argumento uma coleção de dados. Desta forma, ele saberá
#que precisará antes desempacotar estes dados.


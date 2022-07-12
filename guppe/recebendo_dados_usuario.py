"""
Recebendo dados do usuário

input() -> Todo dado reccebido vai input é do tipo String

EM Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos;
- Aspas simples -> 'Angelina Jolie'
- Asaps duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# - Aspas duplas triplas -> """ Angelina Jolie"""

# Entrada de dados
# print("Qual o seu nome? ")
# nome = input() # Input -> Entrada

nome = input("Qual o seu nome: ")

# Exemplo de print 'antigo' 2.x
# print("Seja bem-vindo %s" % nome)

# Exemplo de print 'moderno' 3.x
# print("Seja bem-vindo(a) {0}".format(nome))

# Exemplo de print 'mais atual' 3.7
print(f"Seja bem-vindo (a) {nome}")

# print("Qual a sua idade:")
# idade = input()

idade = int(input("Qual a sua idade?"))
# Processsamento

# Saida
# Exemplo de print 'antigo' 2.x
# print("%s tem %s anos" % (nome, idade))

# Exemplo de print 'moderno' 3. x
# print("{0} tem {1} anos".format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f"{nome} tem {idade} anos")

"""
# int(idade) => cast

Cast é a 'conversao' de um tipo de dado para outro. 
"""
print(f"{nome} nasceu em {2020 - idade}")

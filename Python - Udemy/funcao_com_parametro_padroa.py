"""
Funções com Parâmetros Padrão (Default Paramters)

- Funções onde a passagem de parâmetros seja opcional
print("Geek University")

print()

# Exemplo de função onde a passagem de parâmetros seja obrigatória
def quadrado(numero):
    return numro ** 2

print(quadrado(3))
pritn(quadrado()) TypeError

def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencia(3)) # Por padrão eleva ao quadrado
print(exponencia(3, 5)) # Eleva a potencia informada pelo usuário

OBS:
Se o usuário passar somente 1 argumento, este será atribuído ao parâmetro número, e será calculado o quadrado deste número;
Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro número e o segundo parâmetro potencia, Então será
calculada esta potência.

print(exponencial())

OBS: Em funçôes Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

#ERRO
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

Exemplos mais complexos

def mostra_informcao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek:
        return 'Eu pensei que você era o instrutor'
    return f'OLá {nome}

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany))

Por utilizar parÂmetros com valor default

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis para parâmetros;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dado:
    - Números, strings, floats, booleans, listas, tuplas, dicionários, funções e etc;

# Escopo - Evitar problemas e confusões ...

# Variáveis globais
# Variávies locais

instrutor = 'Geek' # Variável global

def diz_oi():
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

# Atenção com variáveis globais (Se puder evitar, evite)

total = 0

def incremento():
    total += 1 # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incremento())

total = 0

def incremento():
    global total # Avisando que queremos utilizar a variável global
    total += 1 
    return total

print(incremento())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonLocal contador
        contador += 1
        return contador
    return dentro()

print(fora())

"""
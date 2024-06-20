"""
1
def dobro(num):
    return num * 2

2
def dataFor():
    '''
    - Essa função pega a data atual e coloca ela em extenso
    - O date.today pega a data no sistema 
    - O strftime pega a data e coloca ela em extenso
    - O strftime tem que ser passado um parametro que é o formato da data
    '''
    import datetime as ds
    data_str = ds.date.strftime(ds.date.today(),'Hoje é dia %d de %B de %Y')
    return data_str

print(dataFor())

3
def posiNeg(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
    
print(posiNeg(0))

4
def quadradroPerf(num):
    tenta = 0
    for n in range(1,101):
        tenta += 1
        if num > 0 and num // n == n:
            return f'{num} é um quadrado perfeito'
        elif tenta == 100:
            return f'{num} não é um quadrado perfeito'
        
print(quadradroPerf(35))

5
def volume_esfera(raio):
    # Descobrindo o valor do volume de uma esfera
    from math import pi
    return (4/3)*pi*(raio**3)

volum = float(input('Digite o raio para descobrir o volume: '))
print(f'O volume da esfera é {volume_esfera(volum):.2f} cm³')

6
def convert_segundo(hora, minutos):
    # Convertendo hora e minutos para segundos
    return f'''{hora} hora(s) tem = {hora * 3600} segundos
{minutos} minutos tem = {minutos * 60} segundos'''

hora = int(input('Digite a hora: '))
minu = int(input('Digite os minutos: '))
print(convert_segundo(hora, minu))

7
def tempera_Fahre(celsi):
    # Convertendo a temperatura para fahrenheit
    return (celsi * 9/5) + 32

cel = float(input('Digite a temperatura: '))
print(f'A temperatura em Fahrenheit é {tempera_Fahre(cel)}°F')

8
def hipotenusa(areaA, areaB):
    #calculando a hipotenusa
    return (areaA**2 + areaB**2) ** (1/2)

area = float(input('Digite o valor do lado A: '))
areab = float(input('Digite o valor do lado B: '))
print(f'A hipotenusa é {hipotenusa(area, areab)}')

9
def volume_cilindro(raio, altura):
    # Calculando o volume de um cilindro
    from math import pi
    return pi * (raio ** 2) * altura

ra = float(input('Digite o raio do cilindro: '))
al = float(input('Digite a altura do cilindro: '))
print(f'O volume do cilindro é {volume_cilindro(ra, al):.2f} cm³')

10
def maior(num1, num2):
    # Verificando qual número é maior
    return num1 if num1 > num2 else num2

num = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
print(f'O maior numero é {maior(num, num2)}')

11
def mediaAluno(nota1, nota2, nota3, modo):
    '''Calculando a média do aluno
    - O modo irá escolher se fará média aritmética ou média ponderada'''
    if modo == 'A':
        return (nota1 + nota2 + nota3) / 3
    elif modo == 'P':
        return (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
    
nota = float(input('Digite a 1 nota do aluno: '))
nota2 = float(input('Digite a 2 nota do aluno: '))
nota3 = float(input('Digite a 3 nota do aluno: '))
modo = input('Digite A para aritmética ou P para ponderada: ').upper()
print(f'A média do aluno é {mediaAluno(nota, nota2, nota3, modo)}')

12
def somaDosNumeros(num):
    # Soma de todos os algaritmos do número
    soma = 0
    if num > 0:
        num = str(num) # tranforma o numero em string para passar no for 
        for x in num:
            soma += int(x) # tranforma em inteiro de novo para fazer a soma
        return soma
    else:
        return 'Número inválido'
   
numer = int(input('Digite um número: '))
print(f'A soma dos algaritmos do número {numer} é {somaDosNumeros(numer)}')

13
def calculado(numero1, numero2, simbolo):
    # Retorna o resultado da operação que foi escolhida 
    if simbolo == '+':
        return numero1 + numero2
    elif simbolo == '-':
        return numero1 - numero2
    elif simbolo == '*':
        return numero1 * numero2
    elif simbolo == '/':
        return numero1 / numero2
    else:
        return 'Operação inválida'
    
num1 = int(input('DIgite um número: '))
num2 = int(input('Digite outro número: '))
simb = input('''Escolha a operação:
+ para soma
- para subtração
* para mulpicação
/ para divisão: ''')
print(f'O resultado da operação é {calculado(num1, num2, simb)}')

14
def calcularConsumo(distancia, litros):
    # Calcula o consumo de um carro litros por distância
    consum = distancia / litros
    print(f'[{"CONSUMO":^10}][{"(Km/l)":^10}][{"MENSAGEM":^18}]')
    if consum < 8:
        print(f'[{"menor que":^10}][{"8":^10}][{"Venda o Carro!":^18}]')
    elif consum >= 8 and consum <= 12:
        print(f'[{"entre":^10}][{"8 e 12":^10}][{"Econômico!":^18}]')
    elif consum > 12 :
        print(f'[{"maior":^10}][{"12":^10}][{"Super Econômico!":^18}]')

dis = float(input('Digite a distância Km: '))
lit = float(input('Digite a quantidade de litros: '))
calcularConsumo(dis, lit)

15
def maiorQ_0(numero):
    # Verifica se o número é maior que 0 se não for irá entrar no loop até ser maior
    while numero <= 0:
        numero = float(input('Digite um número maior que 0: '))
    return numero

def confirmTriangu(ladoA, ladoB, ladoC):
    # Verifica se os lados formam um triângulo
    if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
        definirTriangulo(ladoA, ladoB, ladoC)
    else:
        print('Os lados não formam um triângulo')

def definirTriangulo(ladoA, ladoB, ladoC):
    # Verifica qual o tipo de triângulo
    if ladoA == ladoB == ladoC:
        print('Triângulo Equilátero')
    elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')


areaA = maiorQ_0(float(input('Digite um número maior que 0: ')))
areaB = maiorQ_0(float(input('Digite um número maior que 0: ')))
areaC = maiorQ_0(float(input('Digite um número maior que 0: ')))
confirmTriangu(areaA, areaB, areaC)

16
def desenhaLinha(num):
    # Desenha uma linha de tamanho num
    print('='*num)

desenhaLinha(18)

17
def maiorQ_0(numero):
    # Verifica se o número é maior que 0 se não for irá entrar no loop até ser maior
    while numero <= 0:
        numero = int(input('Digite um número maior que 0: '))
    return numero

def somaNume(numero, numero1):
    # Soma os números digitados
    somanu = []
    somanu.append(numero + numero1)
    soma1 = soma2 = 0
    for num in str(numero):
        num = int(num)
        soma1 += num
    somanu.append(soma1)
    for num in str(numero1):
        num = int(num)
        soma2 += num
    somanu.append(soma2)
    return somanu

nume1 = maiorQ_0(int(input('Digite um numero maior que 0: ')))
nume2 = maiorQ_0(int(input('Digite um numero maior que 0: ')))
resul = somaNume(nume1, nume2)

print(f'A soma dos números existentes entre {nume1} e {nume2} é :', end=' ')
for num in resul:
    print(num, end=' ')

18
def exponen(x, z):
    # Calcula a exponenciação de x elevado a z
    if z == 0:
        return 1
    else:
        return x ** z
    
print(exponen(0, 0))

19
def maiorFatPrim(num):
    # Retorna o maior fator primo
    if num == 1:
        return 1
    else:
        for i in range(2, num):
            if num % i == 0:
                return maiorFatPrim(num // i)
        return i + 1

n = 600851475143       
print(maiorFatPrim(n))

20
def fatorial(num):
    # Calcula o fatorial de um número
    soma = 1
    if num == 0:
        return 1
    else:
        for nu in range(2, num + 1):
            soma *= nu
        return soma

print(fatorial(5))

21
def numPrimo(num):
    # Verifica se um número é primo
    primo = []
    if num == 2:
        primo.append(num)
    else:
        for i in range(2, num + 1):
            pri = 0
            for j in range (2, num + 1):
                if i % j == 0:
                    pri += 1
                    if pri == 1:
                        primo.append(i)
                    elif pri == 2:
                        primo.pop()
    return len(primo) + 1

n = 11
print(f'A quantidade de números primos de 1 até {n} é : {numPrimo(n)}')

22
def desenha(num):
    for i in range(1, num + 1):
        print('!'*i)

n = desenha(5)

23
def desenhaTRiang(num):
    # Desenha um triângulo
    for i in range(1, num + 1):
        print('*'*i)
    for i in range (num-1, 0, -1):
        print('*'*i)

tri = desenhaTRiang(4)

24
def desenhaTr(num):
    # Desenha um triângulo
    # MEU
    for i in range(1, num + 1):
        if i == 1:
            print(f"{'*'*i:>{num}}")
        else:
            print(f"{'*'*i:>{num}}", end='')
            print(f"{'*'*(i - 1)}")
            
b = desenhaTr(6)

def gerar_triangulo(n):
    # ChatGPT
    # Iterar sobre cada linha do triângulo
    for i in range(n):
        # Calcular o número de espaços e asteriscos para a linha atual
        espacos = n - i - 1
        asteriscos = 2 * i + 1
        
        # Gerar a linha com os espaços e asteriscos
        linha = ' ' * espacos + '*' * asteriscos
        
        # Imprimir a linha
        print(linha)

# Exemplo de uso
n = 6
gerar_triangulo(n)

25
def calcula(num):
    # Calcula a soma de uma operação
    resul = 2 / 4 + 5 / 5 + 10 / 6 + ((num ** 2) + 1) / (num + 3)
    return resul

soma = calcula(5)
print(f'O resultado é {soma:.2f}')

26
def calculeSomator(numero):
    # Calcula a soma de 1 até o número selecionado
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma

num = 5
print(f'A somatória de 1 ate {num} é {calculeSomator(num)}')

27
from math import *
def senoTaylor(x):
    # Calcula o seno de um número usando a série de Taylor
    nume = 10
    sen_x = 0
    for i in range(nume):
        sen_x += pow(-1,i) * pow(x,2*i+1) / factorial((2*i+1))
    return f'{sen_x:.10f}'
    

x_dreg = float(input('Digite o valor em graus: '))
print(f'{senoTaylor(x_dreg)}')


28 


"""
from math import *

def cos(x, n):
    # Calcula o cosseno de um número usando a série de Taylor
    nume = n
    sen_x = 0
    for i in range(nume):
        sen_x += pow(-1,i) * pow(x,2*i+1) / factorial


def cos(x, n):
  formula = lambda k: (-1)**k * x**(2*k) / factorial(2*k)
  soma = 0

  for k in range(n+1):
    soma += formula(k)

  return soma


"""num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))
num3 = int(input("Digite outro número inteiro:"))
soma = num1 + num2 + num3
print(f"A soma dos números {num1}, {num2} e {num3} é {soma}")

num = float(input("Digite um número e saiba o quadarado desse numero: "))
print(num ** 2)

num = float(input("Digite um numero: "))
divi = (num / 5)
print(f"A quinta parte do numero {num} é {divi}")

cel = float(input("Digite a temperatura: "))
fah = cel * (9.0 / 5.0) + 32.0
print(f"A temperatura em Fahrenheit é {fah}")

fah = float(input("Digite a temperatura em fahrenheit: "))
cel = 5.0 * (fah - 32.0) / 9.0
print(f'A Temperatura em Celsius é {cel}')

kel = float(input("Digite a temperatura em Kelvin: "))
cel = kel -273.15
print(f"A temperatura em Celsius é {cel}")

c = float(input("Digite a temperatura em Celsius: "))
k = c + 273.15
print(f"A temperatura em Kelvin é {k}")

k = int(input("Digite a velocidade do  do veiculo: "))
m = k / 3.6
print(f"Você esta a {m} metros por segunfo")

ms = int(input("Digite a velocidade do  do veiculo: "))
km = ms * 3.6
print(f"Você esta a {km} Km por hora")

k = int(input("Digite a velocidade do  do veiculo: "))
m = k / 1.61
print(f"Você esta a {m} milhas por segunfo")

mi = int(input("Digite a velocidade do  do veiculo: "))
km = 1.61 * mi
print(f"Você esta a {km} km de distância")

g = float(input("Digite um grau: "))
r = 3.14
ra = g * r / 180
print(f"A conversão em radianos é {ra}")

ra = float(input("Digite um grau: "))
g =  ra * 180 / r
print(f"A conversão em graus é {g}")

c = float(input("Digiete o centimetros? "))
p = c / 2.54
print(f"Em polegadas ficou {p}")

po = float(input("Digiete o polegadas? "))
ce = po * 2.54
print(f"Em centimetros ficou {ce}")

m = int(input("Digite o valor m³: "))
l = 1000 * m
print(f"O valor em litros fica {l}")

li = int(input("Digite o valor litros: "))
me = li / 1000
print(f"O valor em m³ fica {me}")

k = float(input("Digite o valor quilograma: "))
l = k / 0.45
print(f"O valor em libras fica {l}")

li = float(input("Digite o valor libras: "))
ki = li * 0.45
print(f"O valor em quilogramas fica {ki}")

j = float(input("Digite o valor jardas: "))
m = 0.91 * j
print(f"O valor em metros fica {m}")

me = float(input("Digite o valor netros: "))
ja = me / 0.91
print(f"O valor em jardas fica {ja}")

mt = float(input("Digite o valor m²: "))
ac = mt * 0.000247
print(f"O valor em acres fica {ac}")

ac = float(input("Digite o valor acres: "))
mtr = ac * 4048.58
print(f"O valor em m² fica {mtr}")

me = float(input("Digite o valor m²: "))
he = me * 0.0001
print(f"O valor em hectares fica {he}")

hec = float(input("Digite o valor hectares: "))
mt = hec * 10000
print(f"O valor em m² fica {mt}")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
soma = (num1 ** 2) + (num2 **2) +(num3 **2)
print(f"A soma do quadrado desses némros é {soma}")

no = float(input("Digite uma nota: "))
no1 = float(input("Digite uma nota: "))
no2 = float(input("Digite uma nota: "))
no3 = float(input("Digite uma nota: "))
med = (no + no1 + no2 + no3) / 4
print(f'A média final é {med}')

re = float(input("Digite o valor em reais: R$ "))
dol = float(input("Digite o valor do dolar: $ "))
co = re / dol
print(f"O valor digitado convertido em dolar fica {co}")

num = int(input("Digite um numero: "))
ant = num - 1
sus = num + 1
print(f"O antecessor do número {num} é {ant} e o sucessor é {sus}")

num = int(input("Digite um numero: "))
ant = num - 1
sus = num + 1
so = (ant ** 2) + (sus ** 3)
print(f'A soma do triplo do sucessor, com o dobro do antecessor é {so}')

la = float(input("Digite umlado do quadrado: "))
ar = la ** 2
print(f"A área do quadrado é {ar}")

ra = float(input("Digite o raio do circulo para saber a sua área: "))
r = 3.14
ar = r * (ra **2)
print(f"A área do circulo é {ar}")

from math import sqrt

a = int(input("Digite o valor do cateto: "))
b = int(input("Digite o valor do cateto: "))
hipo = sqrt((a ** 2) + (b ** 2))
print(f"A hipotenusa é {hipo}")

al = float(input("Digite a altura do cilindro: "))
ra = float(input("Digite o raio do cilindro: "))
r = 3.141592
vo = r * (ra ** 2) * al
print(f'O volume do cilindro é {vo:.2f}')

val = float(input("Digite o valor do produto: "))
des = val - (val * 0.12)
print(f'O produto com desconto de 12% ficou R$ {des}')

sal = float(input("Digite seu salário: R$ "))
au = sal + (sal * 0.25)
print(f"O novo salário é R$ {au}")

to = 780000000
pr = int(to * 0.46)
se = int(to * 0.32)
te = to - pr - se
print(f'O primreiro lugar recebeu {pr:.2f}, o segundo {se:.2f} eo terceiro recebeu {te:.2f}')

di = int(input("digite a quantidade de dias trabalhados: "))
val = 30
imp = (di * val) * 0.08
rec = (di * val) - imp
print(f"O valr recebido por trabalhar {di} dias foi de R$ {rec} tirando os 8% do imposto que é {imp}")

valh = float(input("Quanto você ganha por hora; "))
hom = float(input("Quantas horas você trabalha por mês; "))
porm = (hom * valh)
sal = porm + (porm * 0.1)
print(f'Por mês você recebe R$ {sal} reais')

sal = float(input("Digite o seu salário R$ "))
gra = sal * 0.05
imp = sal * 0.07
rec = sal - imp + gra
print(f"O seu salário base é R${sal} você paga 7% de imposto R$ {imp} e recebe 5% de gratificação {gra} "
      f"\n com isso você recebe ao total R$ {rec:.2f}")

pro = float(input("Digite o valor do produto R$ "))
des = pro - (pro * 0.1)
print(f"Se for avista tem o desconto de 10% o valor irá ficar R$ {des}")
paga = input("Modo de pagamento parcelado? ").lower()
if paga == "s":
    par = pro / 3
    ven = pro * 0.05
    print(f'O valor de cada parcela será {par}')
    print(f'O vendedor irá receberR$ {ven} de comissão sobre o valor')
else:
    ven = des * 0.05
    print(f'O vendedor irá receber R$ {ven} equivalente a 5% do produto')

tam = float(input('Digite o tamanho do degrau: '))
alt = float(input('Digite até que altura você quer chegar: '))
alt = alt * 100
deg = alt / tam
print(f'Você terá que dubir {deg:.2f} degraus')

46 - num = input('Digite um número inteiro positivo de 100 até 999: ')
print(f'O numero digitado foi {num} e ele invertido fica {num[::-1]}')

47 - num = input('Digite um número entre 1000 e 9999: ')
for v in num:
    print(v)

48 - segundo = int(input('Digite um valor em segundos: '))
hor = segundo // 3600
rest_segu = segundo % 3600
minu = rest_segu / 60
seg = rest_segu % 60
print(f'O número digitado tem {hor:.0f} horas, {minu:.0f} minutos e {seg} segundos')

49 - hor = int(input('Diigite em que horas comecou a experiencia: '))
minu = int(input('Os minutos: '))
segu = int(input('Os segundos: '))
temp = int(input('Qual será o tempo de duração em segundos: '))

hr = temp // 3600
segun_rest = temp % 3600
minutos = segun_rest // 60
segun = segun_rest % 60
hora = hor + hr
mi = minu + minutos
seg = segu + segun
if seg >= 60:
    seg -= 60
    mi += 1
if mi >= 60:
    mi -= 60
    hora += 1
if hora >= 24:
    dia = hora // 24
    hora = hora % 24
elif hora < 24:
    dia = 0

print(f'A experiencia vai acabar as {dia} dias, {hora} horas, {mi} minutos e {seg} segundos')

50 - from datetime import date
atual = date.today().year
idade = int(input('Qual a su a idade? '))
nasc = atual - idade
print(f'Você nasceu no ano de {nasc}')
"""
comp = float(input('Digite o comprimento do terreno: '))
lar = float(input('Digite a largura do terreno '))
mettla = float(input('Digite o valor do metro da tela R$ '))
metr = comp * lar
custo = metr * mettla
print(f'Um terreno com {comp}²m de comprimento e {lar}²m de largura ira custar R${custo:.2f} para cercar')


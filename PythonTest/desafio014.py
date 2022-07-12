c = float(input('\033[1;37;40mDigite a temperatura em graus °C:\033[m '))
f = ((9*c)/5)+32
print('\033[35mA temperatura de {}°C corresponde a {}°F!\033[m'.format(c, f))
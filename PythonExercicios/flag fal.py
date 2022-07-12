valido =False

while not valido:
    n = int(input('Digite um número no intervalo [1, 50]: '))
    if 1 <= n and n <= 50:
        valido = True
print('Número aceito')
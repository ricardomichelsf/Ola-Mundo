x = int(input())
n = int(input())
soma = 0
cont = 1
multipl = 0
while soma < n:
    soma = x * cont
    if soma == n or soma > n:
        break
    else:
        multipl += 1
    cont += 1
print(f"O numero {x} tem {multipl} multiplos menores que {n}")

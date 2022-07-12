n = 0
nm = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        nm += 1
        n += c
print(f'A soma de todos os {nm} valores solicitados é {n}')

maxi = 0
mini = 0
for c in range(1, 6):
    kg = float(input('DIgite o seu peso: '))
    if c == 1:
        maxi = kg
        mini = kg
    else:
        if kg > maxi:
            maxi = kg
        if kg < mini:
            mini = kg
print(f'O maior peso foi {maxi}Kg')
print(f'O menor peso digitado foi {mini}Kg')


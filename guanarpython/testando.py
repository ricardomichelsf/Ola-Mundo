frase = "O rato roeu a roupa do rei de roma"
junt = ''.join(frase.split())
tem = len(junt)
x = 0
y = 0
for letra in junt:
    print(f'{junt[0:x]:>27}{junt[0:y]}')
    x += 1
    y += 1
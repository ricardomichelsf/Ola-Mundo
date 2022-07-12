re1 = float(input('Digite a medida de uma reta: '))
re2 = float(input('Digite a medida de outra reta:'))
re3 = float(input('Digite outra reta: '))
if re1 + re2 > re3 and re1 + re3 > re2 and re2 + re3 > re1:
    print('Essas retas formam um triângulo')
else:
    print('Essas retas não formam um triângulo')

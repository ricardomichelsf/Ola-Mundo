m1 = float(input('Digite uma medida: '))
m2 = float(input('Digite uma medida: '))
m3 = float(input('Digite uma medida: '))
if m1 + m2 > m3 and m2 + m3 > m1 and m1 + m3 > m2:
    if m1 == m2 == m3:
        print('Essas medidas formam um triangulo \033[1:30mEQUILATERO\033[m')
    elif m1 != m2 != m3 != m1:
        print('Essas medidas formam um triangulo \033[1:33m ESCALENO\033[m')
    else:
        print('Essas medidas formam um triangulo \033[1:34mISOCELES\033[m')
else:
    print('Essas medidas não formam um triangulo')

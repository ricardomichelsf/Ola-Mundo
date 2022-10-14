from math import cos, sin, tan, radians
num = float(input('Digite um ângulo: '))
co = cos(radians(num))
se = sin(radians(num))
ta = tan(radians(num))
print(f'No ângulo {num}\n Temos \no coseno {co:.2f} \no seno {se:.2f} e \na tangente {ta:.2f}')

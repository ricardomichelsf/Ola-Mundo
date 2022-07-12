import math
pi = math.pi
e = math.e
a = float(input())
b = float(input())
c = float(input())
d = float(input())
i = ((a**2) + 3 * b) / c + d
print(f'i) {round(i, 4)}')
ii = math.log(a, 10) + (e ** (-b / c)) - ((d ** 2) / pi)
print(f'ii) {round(ii, 4)}')
iii = ((a ** (2/3)) * b **(1/3) + (c * d)) / (a + b + c + d)
print(f'iii)', round(iii, 4))
iv = (a + b) * (c + d) / (a * b * c * d)
print(f'iv) {round(iv, 4)}')
v =(a ** 2 + b **2) / (c * d) - (c **2 + d **2) / (a * b)
print(f'v) {round(v, 4)}')
vi = (a + b + c + d) ** 2
print(f'vi) {round(vi, 4)}')
vii = a ** 2 + b ** 2 + c ** 2 + d ** 2
print(f'vii) {round(vii, 4)}')
viii = (a * b * c * d) ** (1/3)
print(f'viii) {round(viii, 4)}')

import math
an = float(input('Digite o ângulo que você deseja: '))
seo = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo de \033[1;36m{}\033[m tem o SENO de {:.2}'.format(an, seo))
print('O ângulo de \033[1;33m{}\033[m tem o COSSENO de {:.2f}'.format(an, cos))
print('O ângulo de \033[1;32m{}\033[m tem a TANGENTE de {:.2f}'.format(an, tan))
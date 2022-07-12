frase = str(input('Digite o seu nome: ')).strip()
div = frase.split()
print('\033[32mSeu nome em maiuscula é {}\033[m'.format(frase.upper()))
print('\033[34mSeu nome em minuscula é {}\033[m'.format(frase.lower()))
print('\033[36mSeu nome tem ao todo {} letras\033[m'.format(len(frase)- frase.count(' ')))
print('\033[33mSeu primeiro nome tem {} letras\033[m'.format(frase.find(' ')))




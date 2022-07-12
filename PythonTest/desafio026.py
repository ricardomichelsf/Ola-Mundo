frase = str(input('Digite uma frase: ')).strip().lower()
print('\033[35mAparecem {} letras "A" na frase\033[m'.format(frase.count('a')))
print('\033[31mA primeira letra "A" apareceu na posição {}\033[m'.format(frase.find('a')+1))
print('\033[36mA última letra "A" apareceu na posição {}\033[m'.format(frase.rfind('a')+1))

frase = input('Digite uma frase: ').strip().lower()
fra = frase.count('a')
fras = frase.find('a')
fr = frase.rfind('a')
print(f'Tem {fra} letra(s) "a"')
print(f'A primeria aparece na posição {fras+1}')
print(f'A ultima aparece na posição {fr+1}')

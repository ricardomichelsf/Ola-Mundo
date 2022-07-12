import math
not1 = float(input())
not2 = float(input())
not3 = float(input())
frequenci = float(input())
presen = frequenci * 100
med1 = not1 * 2
med2 = not2 * 2
med3 = not3 * 3
soma = (med1 + med2 + med3)/ (2 + 2 + 3)
round(soma)
print(f'Frequencia: {presen:.0f}%')
print(f'Media: {soma:.1f}')
if presen >= 75:
    if soma > 9:
        print('Aluno aprovado com louvor!')
    elif soma >= 6 and soma <= 9:
        print('Aluno aprovado!')
    elif soma >= 4:
        print('Aluno de recuperação!')
    else:
        print('Aluno reprovado!')
else:
    print('Aluno reprovado por faltas!')

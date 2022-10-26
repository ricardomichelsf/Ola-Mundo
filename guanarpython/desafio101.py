"""def votar(idad):
    from datetime import date
    atual = date.today().year
    idade = atual - idad
    if idade < 16:
        return f'Com {idade}: Não Vota!'
    elif 16 <= idade < 18 or idade >= 65:
        return f"Com {idade}: Voto Opcional!"
    else:
        return f"Com {idade}: Voto Obrigatorio!!"

print('-='*25)
print('Convacação para votar')
nasc = int(input('Qual o ano que você nasceu? '))
print(votar(nasc))
"""

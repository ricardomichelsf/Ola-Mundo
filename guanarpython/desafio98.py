from time import sleep

def contagem(inic, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {inic} até {fim} de {passo} em {passo}')
    sleep(2)
    if inic < fim:
        contador(inic, fim, passo)   
    else:
        contador(inic, fim, -passo)
        
def contador(inic, fim, pas):
    for cont in range(inic, fim + 1, pas):
        print(f'{cont} ', end='', flush=True) # o flush faz o sleep funcionar d maneira correta sem link tudo
        sleep(0.5)
    print('FIM!')

# resposta do guanabara
"""
def contagem(inic, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {inic} até {fim} de {passo} em {passo}')
    sleep(2)
    if inic < fim:
        cont = 1
        while cont <= fim:
            print(f'{cont} ', end='', fluah=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = 1
        while cont >= fim:
            print(f'{cont} ', end='', fluah=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')
"""

contagem(1, 10 , 1)
contagem(10, 0 , 2)

print('-'*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)


def main():
    num = int(input())
    while num < 1 or num > 9:
        print('Insira um número inicial entre 1 e 9')
        num = int(input())
    return num

def validar(nf, ni):
    if nf >= ni:
        while ni <= nf:
            tabuada(ni)
            print('')
            ni += 1
    else:
        print('Nenhuma tabuada nesse intervalo')

def tabuada(n):
    mult = 1
    while mult <= 9:
        print('{} x {} = {}'.format(n, mult, n * mult))
        mult += 1


n1 = main()
n2 = main()
tabu = validar(n2, n1)

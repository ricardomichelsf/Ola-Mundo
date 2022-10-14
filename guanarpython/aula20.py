def mostralinha(texto):
    print('-'*30)
    print(texto)
    print('-'*30)

mostralinha('Curso em video')
mostralinha('Aprenda Python')
mostralinha('Gustavo Guanabara')

def dobravalores(lis):
    pos = 0
    while pos < len(lis):
        lis[pos] *= 2
        pos += 1
        
valores = [6, 3, 9, 1, 0, 2]
dobravalores(valores)
print(valores)

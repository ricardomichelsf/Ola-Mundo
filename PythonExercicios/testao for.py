def main():
    sequen = input()
    caracte = input()
    quantid = contagemCaract(sequen, caracte)
    return quantid

def contagemCaract(seq, valor):
    cont = 0
    for n in seq:
        if n == valor:
            cont += 1
    return cont

def respost(quanti):
    qtd = main()
    if quanti == 0:
        print("Caractere nao encontrado")
    else:
        print(f'O caractere buscado ocorre {quanti} vezes na sequencia.')


x = respost(main)

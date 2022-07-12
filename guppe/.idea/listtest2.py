produtos = ["aveia", "sabão em pó", "manteiga," "cebola"]
contado = [1, 1, 1, 1]
menu = """\
    Escolha uma opção: 
    (1) Alterarquantidade 
    (2) Sair
"""
escolha = int(input(menu))

while escolha != 2:
    if escolha == 1:
        prod = input("Qual o produto? ")
        if prod in produtos:
            pos = produtos.index(prod)
            quanti = contado[pos]
            print(f'{prod} tem {quanti} unidades')
            nova_qunt = int(input("Nova quantidade: "))
            if nova_qunt == 0:
                produtos.pop(pos)
                contado.pop(pos)
            else:
                contado[pos] = nova_qunt
        else:
            print(f"Ops, A lista não contem este {prod}")   
    else:
        print(f"{escolha} não é valida")
    escolha = int(input(menu))

for i in range(len(produtos)):
    prod = produtos[i]
    quanti = contado[i]
    print(f"{prod} tem {quanti} unidades")
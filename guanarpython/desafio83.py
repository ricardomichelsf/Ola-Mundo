expr = input('Digite uma expresão: ')
pilha = []
for simb in expr:
    if simb =='(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha .append(')')
            break
if len(pilha) == 0:
    print('Essa expressão é válida')
else:
    print('Essa expressão é invalida')


nome = str(input('Digite o nome completo: ')).strip()
nom = nome.split()
print("\033[36mMuito prazer em te conhecer!\033[m ")
print('\033[32mPrimeiro nome: {}\033[m'.format(nom[0]))
print('\033[7;30mÚltimo nome: {}\033[m'.format(nom[-1]))


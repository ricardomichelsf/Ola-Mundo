cid = str(input('\33[36mDigite o nome de uma cidade:\033[m ')).strip()
print(cid[:5].upper() == 'SANTO')
print('\033[32mA cidade digitada foi {}\033[m'.format(cid))


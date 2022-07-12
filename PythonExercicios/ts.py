texto = texto.lower()
texto = texto.replace(" ","")
texto = texto.replace("\n","")
texto = texto.replace(".","")
texto = texto.replace("!","")
texto = texto.replace("?","")
texto = texto.replace(",","")
texto = texto.replace(";","")
texto = texto.replace("á","a")
texto = texto.replace("à","a")
texto = texto.replace("ã","a")
texto = texto.replace("é","e")
texto = texto.replace("ê","e")
texto = texto.replace("í","i")
texto = texto.replace("ó","o")
texto = texto.replace("ô","o")
texto = texto.replace("ú","u")
texto = texto.replace("ç","c")

vogais = 0
consoantes = 0

for caracter in texto:
    if caracter in 'aeiou':
             vogais = vogais + 1
    else:
            consoantes = consoantes + 1

print("Vogais: {}".format(vogais))
print("Consoantes: {}" .format(consoantes))
print("Total de letras: {}".format(vogais+consoantes))
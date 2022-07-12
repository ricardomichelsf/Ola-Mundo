vel = float(input("\033[7;30mDigite a velocidade do carro:\033[m "))
mu = (vel - 80) * 7
ul = vel - 80
if vel > 80:
    print("\033[36mVocê ultrapassou {}km/h acima do limite, \nE foi multado e pagará: {:.2f} reais de multa".format(ul, mu))
print("Tenha um bom dia! Dirija com segurança!\033[m")
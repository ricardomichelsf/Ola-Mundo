salario = float(input('Digite o salário R$ '))
tempo_cliente = int(input('Quanto tempo você é cliente: '))
empresti = float(input('Valor do emprestimo R$ '))
if salario > 2000:
    print('Parabéns o seu emprestimo foi aceito')
    if tempo_cliente > 2:
        juros = empresti * 0.15
    else:
        juros = empresti * 0.20
    empresti = empresti + juros
    parcela = input('Você quer parcelar? [S/N] ').strip().upper()
    if parcela == "s,s":
        tempo_parc = int(input('Em quantos anos você quer pagar: '))
        parc = tempo_parc * 12
    valor = empresti / parc
    print(f'O valor do seu emprestimo ficou R$ {empresti:.2f}, Você irá pagar R$ {valor:.2f} por mês por {parcela} ano(s)')
else:
    print('Desculpe, mas seu emprestimo foi negado pois não atende algum dos requisitos.')

"""
Documentando funções com Docstrings

OBS: Podemos ter acesso á documentação de uma função em Python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso a documentação com a função help()

Exemplos:

def diz_oi():
    '''Uma função simples que retorna a string 'OI' '''
    return 'Oi!'

"""
def exponencial(numero, potencia= 2):
    '''
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á potencia' informa
    :para numero: Número que desejamos gerar o exponencial.
    :para potencia: Potencia que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponencial de 'numero' á 'potencia'
    '''
    return numero ** potencia



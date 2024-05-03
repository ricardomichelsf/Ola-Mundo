# Cria a classe Pessoa para fazer o cadastro
class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

# Essa classe irá criar o cadastro dos médicos e suas especialidades
class Medico(Pessoa):
    def __init__(self, nome, cpf, telefone, crm, especialidade):
        super().__init__(nome, cpf, telefone)
        self.crm = crm
        self.__salario = 0
        self.especialidade = especialidade

    # Ira retornar o salario dos médicos
    def get_salario(self):
        return self.__salario

    # Ira receber o salario
    def set_salario(self, valor):
        self.__salario = valor
"""
    # Recebe a especialidade e coloca na lista
    def especialistas(self, especialidade):
        self.especialidade.append(especialidade)
"""

class Paciente(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, endereco, data_de_nascimento):
        super().__init__(nome, cpf, telefone)
        self.rg = rg
        self.endereco = endereco
        self.data_de_nascimento = data_de_nascimento


class Clinica:
    def __init__(self, quarto, andar):
        self.quarto = quarto
        self.andar = andar


# Cria um prontuario do paciente e do medico
class Internacao(Clinica):
    def __init__(self, quarto, andar, observacao):
        super().__init__(quarto, andar)
        self.observacao = observacao


class Relatorio(Internacao,Paciente, Medico):
    def __init__(self, quarto, andar, observacao, data, horario, nome, cpf, telefone, rg, endereco, data_de_nascimento, crm, especialidade):
        Paciente.__init__(nome, cpf, telefone, rg, endereco, data_de_nascimento)
        Medico.__init__(nome,crm, especialidade)
        Internacao.__init__(quarto, andar, observacao)
        self.data = data
        self.horario = horario
        self.paciente = nome
        self.medico = nome
  

    def exibir_dados(self):
        print(f'O paciente {self.paciente} está internado no quarto {self.quarto}, no {self.andar} andar')
        print(f'O médico responsável {self.medico} com especialidade em {self.especialidade}')
        print(f'Foi visitado no dia {self.data} às {self.horario} horas')


med = Medico('Michel', 445434213, 15410435, 1541, 'Cirurgião')
med.set_salario(11.000)
pac1 = Paciente("Ricardo", 37005967828, 954791603, 16531, 'Cecília Morais', '24/03/88')
clin = Clinica('119', '3°')
inter = Internacao(clin.quarto, clin.andar, 'Recuperação')
rel = Relatorio(pac1.nome, inter.quarto, inter.andar, med.nome, med.especialidade ,'21/01/2023', '08:30')
rel.exibir_dados()

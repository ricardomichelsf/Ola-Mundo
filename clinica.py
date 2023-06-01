# Cria a classe Pessoa para fazer o cadastro
class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

# Essa classe irá criar o cadastro dos médicos e suas especialidades
class Medico(Pessoa):
    def __init__(self, nome, cpf, telefone, crm):
        super().__init__(nome, cpf, telefone)
        self.crm = crm
        self.__salario = 0
        self.especialidade = []

    # Ira retornar o salario dos médicos
    def get_salario(self):
        return self.__salario

    # Ira receber o salario
    def set_salario(self, valor):
        self.__salario = valor

    # Recebe a especialidade e coloca na lista
    def especialistas(self, especialidade):
        self.especialidade.append(especialidade)


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
        self.nome_Paciente = Paciente.nome
        self.nome_Medico = Medico.nome
        self.especialidade_Medico = Medico.especialidade

    def get_nome_Paciente(self):
        return self.nome_Paciente

    def get_nome_Medico(self):
        return self.nome_Medico

    def get_especialidade_Medico(self):
        return self.especialidade_Medico


class Relatorio(Internacao):
    def __init__(self, quarto, andar, observacao, data, horario, nome_Paciente, nome_Medico, especialidade_Medico):
        super().__init__(quarto, andar, observacao, nome_Paciente, especialidade_Medico)
        self.data = data
        self.horario = horario

    def exibir_dados(self):
        nome_paciente = self.get_nome_Paciente()
        nome_medico = self.get_nome_Medico()
        especialidade_medico = self.get_especialidade_Medico()
        print(f'O paciente {nome_paciente} está internado no quarto {self.quarto}, no {self.andar} andar')
        print(f'O médico responsável {nome_medico} com especialidade em {especialidade_medico[0]}')
        print(f'Foi visitado no dia {self.data} às {self.horario} horas')


med = Medico('Michel', 445434213, 15410435, 1541)
med.set_salario(11.000)
med.especialistas('Cirurgião')
pac1 = Paciente("Ricardo", 37005967828, 954791603, 16531, 'Cecília Morais', '24/03/88')
clin = Clinica('119', '3°')
inter = Internacao(clin.quarto, clin.andar, 'Recuperação')
rel = Relatorio(inter.quarto, inter.andar, inter.observacao, '21/01/2023', '08:30', inter.get_nome_Paciente(), inter.get_nome_Medico(), inter.get_especialidade_Medico())
rel.exibir_dados()

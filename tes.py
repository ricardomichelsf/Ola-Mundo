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
        self.especialidade = especialidade


class Paciente(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, endereco, data_de_nascimento):
        super().__init__(nome, cpf, telefone)
        self.rg = rg
        self.endereco = endereco
        self.data_de_nascimento = data_de_nascimento


class Quarto:
    def __init__(self, numero):
        self.numero = numero
        self.paciente = None


class Andar:
    def __init__(self, numero):
        self.numero = numero
        self.quartos = [Quarto(i) for i in range(1, 6)]


class Internacao:
    def __init__(self, paciente, medico, andar, quarto, observacao):
        self.paciente = paciente
        self.medico = medico
        self.andar = andar
        self.quarto = quarto
        self.observacao = observacao


class Relatorio:
    def __init__(self, paciente, medico, andar, quarto, data, horario, observacao):
        self.paciente = paciente
        self.medico = medico
        self.andar = andar
        self.quarto = quarto
        self.data = data
        self.horario = horario
        self.observacao = observacao


if __name__ == "__main__":
    medico1 = Medico("Dr. João", "123456789", "111111111", "CRM123", "Cardiologista")
    medico2 = Medico("Dr. Maria", "987654321", "222222222", "CRM456", "Pediatra")

    paciente1 = Paciente("Fulano", "11111111111", "333333333", "12345", "Rua A", "01/01/1990")
    paciente2 = Paciente("Ciclano", "22222222222", "444444444", "54321", "Rua B", "02/02/1985")

    andar1 = Andar(1)
    andar2 = Andar(2)

    internacao1 = Internacao(paciente1, medico1, andar1, andar1.quartos[0], "Observação do paciente")
    internacao2 = Internacao(paciente2, medico2, andar2, andar2.quartos[2], "Observação do paciente")

    relatorio1 = Relatorio(paciente1, medico1, andar1, andar1.quartos[0], "01/05/2023", "08:30", "Paciente em observação")
    relatorio2 = Relatorio(paciente2, medico2, andar2, andar2.quartos[2], "02/05/2023", "09:00", "Paciente em observação")

    print("Informações sobre a Clínica:")
    print("---- Médicos ----")
    print(f"Médico 1: {medico1.nome} - CRM: {medico1.crm} - Especialidade: {medico1.especialidade}")
    print(f"Médico 2: {medico2.nome} - CRM: {medico2.crm} - Especialidade: {medico2.especialidade}")
    print("---- Pacientes ----")
    print(f"Paciente 1: {paciente1.nome} - CPF: {paciente1.cpf} - RG: {paciente1.rg}")
    print(f"Paciente 2: {paciente2.nome} - CPF: {paciente2.cpf} - RG: {paciente2.rg}")
    print("---- Internações ----")
    print(f"Internação 1: Paciente {internacao1.paciente.nome} - Médico {internacao1.medico.nome} - Andar {internacao1.andar.numero} - Quarto {internacao1.quarto.numero} - Observação: {internacao1.observacao}")
    print(f"Internação 2: Paciente {internacao2.paciente.nome} - Médico {internacao2.medico.nome} - Andar {internacao2.andar.numero} - Quarto {internacao2.quarto.numero} - Observação: {internacao2.observacao}")
    print("---- Relatórios ----")
    print(f"Relatório 1: Paciente {relatorio1.paciente.nome} - Médico {relatorio1.medico.nome} - Andar {relatorio1.andar.numero} - Quarto {relatorio1.quarto.numero} - Data: {relatorio1.data} - Horário: {relatorio1.horario} - Observação: {relatorio1.observacao}")
    print(f"Relatório 2: Paciente {relatorio2.paciente.nome} - Médico {relatorio2.medico.nome} - Andar {relatorio2.andar.numero} - Quarto {relatorio2.quarto.numero} - Data: {relatorio2.data} - Horário: {relatorio2.horario} - Observação: {relatorio2.observacao}")


class DadosPessoais:
    """Classe para gerenciar dados pessoais"""

    def __init__(self, nome, dataNasc, cpf, rg, sexo, telefone):
        """Inicia uma nova instancia com dados pessoais"""
        self.__nome = nome
        self.__nasc = dataNasc
        self.__cpf = cpf
        self.__rg = rg
        self.__sexo = sexo
        self.__fones = []
        self.__fones.append(telefone)
        self.__cel = celular

    def getNome(self):
        """Retorna o nome"""
        return self.__nome
    def setNome(self, novoNome):
        """Edita o nome"""
        self.__nome = novoNome

    def getNasc(self):
        """Retorna a instancia Data com a data de nascimento"""
        return self.__nasc

    def getCpf(self):
        """Retorna a instancia CPF"""
        return self.__cpf
    def setCpf(self, novoCpf):
        """Altera a instancia CPF"""
        self.__cpf = novoCpf

    def getRg(self):
        """Retorna o numero de rg"""
        return self.__rg
    def setRg(self, novoRg):
        """Edita o numero de rg"""
        self.__rg = novoRg

    def getSexo(self):
        """Retorna o sexo"""
        return self.__sexo
    def setSexo(self, novoSexo):
        """Edita o sexo"""
        self.__sexo = novoSexo

    def getFones(self):
        """Retorna a lista de instancias fone intancia telfone"""
        return self.__fones

class Escola:
    """Classe para gerenciar os dados da escola"""

    def __init__(self, rs, cnpj, proprietario, cpf, endereco):
        """inicia os dados da escola"""
        self.__rs = rs
        self.__cnpj = cnpj
        self.__prop = proprietario
        self.__cpf = cpf
        self.__endereco = endereco

    def getRs(self):
        """Retorna a Razao Social da escola"""
        return self.__rs
    def setRs(self, novaRs):
        """Edita a Razao Social da escola"""
        self.__rs = novaRs

    def getCnpj(self):
        """Retorna o CNPJ da escola"""
        return self.__cnpj
    def setCnpj(self, novoCnpj):
        """Edita o CNPJ da escola"""
        self.__cnpj = novoCnpj

    def getProp(self):
        """Retorna o nome do Proprietario da escola"""
        return self.__prop
    def setProp(self, novoProprietario):
        """Edita o nome do Proprietario da escola"""
        self.__prop = novoProprietario

    def getCpf(self):
        """Retorna o CPF do proprietario"""
        return self.__cpf
    def setCpf(self, novoCpf):
        """Edita o CPF do proprietario"""
        self.__cpf = novoCpf

    def getEndereco(self):
        """Retorna a instancia endereco do colegio"""
        return self.__endereco
    def setEndereco(self, novoEndereco):
        """Edita a instancia endereco do colegio"""
        self.__endereco = novoEndereco

class Endereco:
    """Classe para gerencia os enderecos"""

    def __init__(self, rua, numero, bairro, cidade, estado, cep, pais = 'Brasil', infoAdd = None, complemento = None):
        """Inicia um novo endereco"""
        self.__rua = rua
        self.__num = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__uf = estado
        self.__pais = pais
        self.__cep = cep
        self.__comp = complemento
        self.__infoAdd = infoAdd

    def getRua(self):
        """Retorna a rua"""
        return self.__rua
    def setRua(self, novaRua):
        """Edita o nome da rua"""
        self.__rua = novaRua

    def getNum(self):
        """Retorna o numero da residencia"""
        return self.__num
    def setNum(self, novoNumero):
        """Edita o numero da residencia"""
        self.__num = novoNumero

    def getBairro(self):
        """Retorna o nome do bairro"""
        return self.__bairro
    def setBairro(self, novoBairro):
        """Edita o nome do bairro"""
        self.__bairro = bairro

    def getCidade(self):
        """Retorna o nome da cidade"""
        return self.__cidade
    def setCidade(self, novaCidade):
        """Edita o nome da cidade"""
        self.__cidade = novaCidade

    def getUf(self):
        """Retorna o nome do estado do cliente"""
        return self.__uf
    def setUf(self, novoEstado):
        """Edita o nome do estado"""
        self.__uf = novoEstado

    def getPais(self):
        """Retorna o nome do pais"""
        return self.__pais
    def setPais(self, novoPais):
        """Edita o nome do pais"""
        self.__pais = novoPais

    def getCep(self):
        """Retorna o cep"""
        return self.__cep
    def setCep(self, novoCep):
        """Edita o cep"""
        self.__cep = novoCep

    def getComp(self):
        """Retorna o complemento do endereco"""
        return self.__comp
    def setComp(self, novoComplemento):
        """Edita o complemento do endereco"""
        self.__comp = novoComplemento

    def getInfo(self):
        """Retorna informacoes adicionais do endereco"""
        return self.__infoAdd
    def setInfor(self, novaInformacao):
        """Edita as informacoes adicionais do endereco do cliente"""
        self.__infoAdd = novaInformacao

import db

class Endereco:
    """Classe que gerencia os Enderecoes"""
    def __init__(self, ide = None):
        
    def getId(self):
        """Retorna o ID do endereco"""
        return self.__id
    def setId(self, novoId):
        """Ajusta o valor do ID"""
        self.__id = int(novoId)

    def getRua(self):
        """Retorna a Rua"""
        return self.__rua
    def setRua(self, novoRua):
        """Ajusta a rua"""
        self.__rua = str(novoRua)

    def getNum(self):
        """Retorna o numero"""
        return self.__num
    def setNum(self, novoNum):
        """Ajusta o numero"""
        self.__num = int(novoNum)

    def getBairro(self):
        """Retorna o bairro"""
        return self.__bairro
    def setBairro(self, novoBairro):
        """Ajusta o bairro"""
        self.__bairro = str(novoBairro)

    def getCidade(self):
        """Retorna a cidade"""
        return self.__cidade
    def setCidade(self, novoCidade):
        """Ajusta a vidade"""
        self.__cidade = str(novoCidade)

    def getUf(self):
        """Retorna a Unidade Federal"""
        return self.__uf
    def setUf(self, novoUf):
        """Ajusta o Estado"""
        if len(novoUf) is 2:
            self.__uf = str(novoUf)

    def getCep(self):
        """Retorna o CEP"""
        return self.__cep
    def setCep(self, novoCpe):
        """Ajusta o CEP"""
        if len(novoCep) is 8:
            self.__cep = str(novoCpe)

    def getComp(self):
        """Retorna o complemento do endereco"""
        return self.__complemento
    def setComp(self, novoComp):
        """Ajusta o complemento"""
        self.__comp = str(novoComp)

    def carregar(self, ide):
        """Retorna uma tupla do banco de dados"""
        self.__id = int(ide)
        self.cursor.execute("SELECT * FROM DATAS WHERE ID = %s;", (self.__id))
        if self.cursor.rowcount == 1:
            return self.cursor.fetchone()
        else:
            return None

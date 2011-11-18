'''
Created on 15/11/2011

@author: Grupo Sistema Academico
'''

from db import db

class Endereco:
    """Classe que gerencia os Enderecos"""
    def __init__(self, ide = None):
        """Inicia uma instancia Endereco"""
        self.__DataBase = db()
        if ide is None:
            self.setId(None)
            self.setRua(None)
            self.setNum(None)
            self.setBairro(None)
            self.setCidade(None)
            self.setUf(None)
            self.setCep(None)
            self.setComp(None)
        else:
            self.carregar(ide)
            self.setId(ide)
            
    def getId(self):
        """Retorna o ID do endereco"""
        return self.__id
    def setId(self, novoId):
        """Ajusta o valor do ID"""
        self.__id = novoId

    def getRua(self):
        """Retorna a Rua"""
        return self.__rua
    def setRua(self, novoRua):
        """Ajusta a rua"""
        self.__rua = novoRua

    def getNum(self):
        """Retorna o numero"""
        return self.__num
    def setNum(self, novoNum):
        """Ajusta o numero"""
        self.__num = novoNum

    def getBairro(self):
        """Retorna o bairro"""
        return self.__bairro
    def setBairro(self, novoBairro):
        """Ajusta o bairro"""
        self.__bairro = novoBairro

    def getCidade(self):
        """Retorna a cidade"""
        return self.__cidade
    def setCidade(self, novoCidade):
        """Ajusta a vidade"""
        self.__cidade = novoCidade

    def getUf(self):
        """Retorna a Unidade Federal"""
        return self.__uf
    def setUf(self, novoUf):
        """Ajusta o Estado"""
        self.__uf = novoUf

    def getCep(self):
        """Retorna o CEP"""
        return self.__cep
    def setCep(self, novoCpe):
        """Ajusta o CEP"""
        self.__cep = novoCpe

    def getComp(self):
        """Retorna o complemento do endereco"""
        return self.__comp
    def setComp(self, novoComp):
        """Ajusta o complemento"""
        self.__comp = novoComp

    def carregar(self, ide):
        """Carrega endereco a partir de id no BD"""
        self.__dados = self.__DataBase.carregarEndereco(ide)
        if self.__dados == None:
            return False
        else:
            self.setRua(self.__dados[1])
            self.setNum(self.__dados[2])
            self.setBairro(self.__dados[3])
            self.setCidade(self.__dados[4])
            self.setUf(self.__dados[5])
            self.setCep(self.__dados[6])
            if self.__dados[7] == None:
                self.setComp(None)
            else:
                self.setComp(self.__dados[7])
            return True

    def salvarEdit(self, ide):
        """Salva ajuste no endereco no BD"""
        return self.__DataBase.editarEndereco(int(ide), self.getRua(), self.getNum(), self.getBairro(), self.getCidade(), self.getUf(), self.getCep(), self.getComp())

    def addNova(self):
        """Cria um novo endereco no BD"""
        return self.__DataBase.addEndereco(self.getRua(), self.getNum(), self.getBairro(), self.getCidade(), self.getUf(), self.getCep(), self.getComp())

    def delete(self, ide):
        """Deleta um banco a partir de sua ID"""
        return self.__DataBase.delEndereco(ide)

    def pegarId(self):
        """Retorna uma lista com todas as IDs"""
        return self.__DataBase.returnIdEndereco()

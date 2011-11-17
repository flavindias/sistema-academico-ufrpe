'''
Created on 15/11/2011

@author: Grupo Sistema Academico
'''

from db import db

DataBase = db()

class DadosPessoais:
    """Classe que gerencia os dados Pessoais"""
    def __init__(self, documento = None):
        """Inicia uma nova instancia"""
        if documento is None:
            self.setNome(None)
            self.setDataNascId(None)
            self.setDocumento(None)
            self.setSexo(None)
            self.setCelular(None)
            self.setFixo(None)
            self.setEnderecoId(None)
        else:
            self.carregar(documento)
            self.setDocumento(documento)

    def getNome(self):
        """Retorna o nome"""
        return self.__nome
    def setNome(self, novoNome):
        """Ajusta o nome"""
        self.__nome = novoNome

    def getDataNascId(self):
        """Retorna Id de nascimento"""
        return self.__dataNascId
    def setDataNascId(self, novoDataNascId):
        """Ajusta a id de nascimento"""
        self.__dataNascId = novoDataNascId

    def getDocumento(self):
        """Retorna o documento"""
        return self.__documento
    def setDocumento(self, novoDocumento):
        """Ajusta o documento"""
        self.__documento = novoDocumento

    def getSexo(self):
        """Retorna o sexo: 1 HOMEM, 0 MULHER"""
        return self.__sexo
    def setSexo(self, novoSexo):
        """Ajusta o sexo: 1 HOMEM, 0 MULHER"""
        self.__sexo = novoSexo

    def getCelular(self):
        """Retorna o numero de celular"""
        return self.__celular
    def setCelular(self, novoCelular):
        """Ajusta o numero de celular"""
        self.__celular = novoCelular

    def getFixo(self):
        """Retorna o numero do fixo"""
        return self.__fixo
    def setFixo(self, novoFixo):
        """Ajusta o numero fixo"""
        self.__fixo = novoFixo

    def getEnderecoId(self):
        """Retornna id de endereco"""
        return self.__enderecoId
    def setEnderecoId(self, novoEnderecoId):
        """Ajusta o ID de endereco"""
        self.__enderecoId = novoEnderecoId

    def addNova(self):
        """Cria um novo endereco no BD"""
        return DataBase.addDadosPessoais(self.getDocumento(), self.getNome(), self.getSexo(), self.getNascId(), self.enderecoId(), celular = self.getCelular(), fixo = self.getFixo())
    
    def salvarEdit(self, documento):
        """Salva ajuste de endereco no BD"""
        return DataBase.editarDadosPessoais(documento, nome=self.getNome(), sexo=self.getSexo(), dataNascId=self.getDataNascId(), enderecoId = self.getEnderecoId(), celular=self.getCelular(), fixo=self.getFixo())
        
    def carregar(self, documento):
        """Carrega data a partir de id no BD"""
        self.__dados = DataBase.carregarDadosPessoais(documento)
        if self.__dados == None:
            return False
        else:
            self.setDocumento(self.__dados[0])
            self.setNome(self.__dados[1])
            self.setSexo(self.__dados[2])
            self.setCelular(self.__dados[3])
            self.setFixo(self.__dados[4])
            self.setDataNascId(self.__dados[5])
            self.setEnderecoId(self.__dados[6])
            return True

'''
Created on 15/11/2011

@author: Grupo Sistema Academico
'''

from db import db

DataBase = db()

class Data:
    """Classe para gerenciar entradas de datas"""

    def __init__(self, ide = None):
        """inicia uma Instancia Data carregando ou nao do BD"""
        if ide == None:
            self.setId(None)
            self.setAno(None)
            self.setMes(None)
            self.setDia(None)
            self.setHora(None)
        else:
            self.carregar(int(ide))
            self.setId(None)

    def getId(self):
        """Retorna ID da data da instancia"""
        return self.__id
    def setId(self, novoId):
        """Ajusta o ID da data da instancia"""
        self.__id = novoId
    
    def getAno(self):
        """Retorna Ano da data da instancia"""
        return self.__ano
    def setAno(self, novoAno):
        """Ajusta o Ano da instancia"""
        self.__ano = novoAno
    
    def getMes(self):
        """Retorna o Mes da data da instancia"""
        return self.__mes
    def setMes(self, novoMes):
        """Ajusta o Mes da instancia"""
        self.__mes = novoMes
    
    def getDia(self):
        """Retorna o Dia da data da instancia"""
        return self.__dia
    def setDia(self, novoDia):
        """Ajusta o Dia da instancia"""
        self.__dia = novoDia
    
    def getHora(self):
        """Retorna a Hora da instancia"""
        return self.__hora
    def setHora(self, novoHora):
        """Ajusta a Hora da instancia"""
        self.__hora = novoHora

    def addNova(self):
        """Cria uma nova data no BD"""
        if DataBase.addData(self.getAno(), self.getMes(), self.getDia(), self.getHora()):
            return True
        else:
            return False
    
    def salvarEdit(self, ide):
        """Salva ajuste de hora no BD"""
        if DataBase.editarData(int(ide), self.getAno(), self.getMes, self.getDia, self.getHora()):
            return True
        else:
            return False
        
    def carregar(self, ide):
        """Carrega data a partir de id no BD"""
        self.__dados = DataBase.carregarData(int(ide))
        if self.__dados == None:
            return False
        else:
            self.setId(self.__dados[0])
            self.setAno(self.__dados[1].year)
            self.setMes(self.__dados[1].month)
            self.setDia(self.__dados[1].day)
            if self.__dados[2] == None:
                self.setHora(None)
            else:
                self.setHora(str(self.__dados[2]))
            return True

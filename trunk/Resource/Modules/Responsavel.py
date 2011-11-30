#!/usr/bin/env python
#-*-coding: latin1-*-
"""
Created on 15/11/2011

@author: Grupo Sistema Academico
"""
class Responsavel:
    """Classe para Gerenciamento de Conta do Responsavel"""
    def __init__(self, ide):
        """Retorna Id do Professor"""
        self.__DataBase = db()
        if ide is None:
            self.__id = None # INT
            self.__dadosId = None # STR
            self.__loginId = None # STR
        else:
            self.carregar(ide)
            self.setId(ide)

    def getId(self):
        """Retorna Id"""
        return self.__id
    def setId(self, novoId):
        """Edita Id"""
        self.__id = novoId

    def getDadosId(self):
        """Retorna dadosId"""
        return self.__dadosId
    def setDadosId(self, novoDadosId):
        """Edita dadosId"""
        self.__dadosId = novoDadosId

    def getLoginId(self):
        """Retorna Id do Login"""
        return self.__loginId
    def setLoginId(self, novoLoginId):
        """Edita Id do Login"""
        self.__loginId = novoLoginId

    def carregar(self, ide):
        """Carrega responsavel a partir de id no BD"""
        self.__dados = self.__DataBase.carregarResponsavel(ide)
        if self.__dados == None:
            return False
        else:
            self.setId(self.__dados[0])
            self.setDadosId(self.__dados[1])
            self.setLoginId(self.__dados[2])
            return True

    def salvarEdit(self, ide):
        """Salva ajuste de responsavel no BD"""
        return self.__DataBase.editarResponsavel(ide, self.getDadosId(), self.getLoginId())

    def addNovo(self):
        """Cria um novo responsavel no BD"""
        return self.__DataBase.addResponsavel(self.getDadosId(), self.getLoginId())

    def delete(self, ide):
        """Deleta um responsavel a partir da ID"""
        return self.__DataBase.delResponsavel(ide)

    def pegarId(self):
        """Retorna uma lista com todas as IDs de responsaveis"""
        return self.__DataBase.returnIdResponsavel()
#!/usr/bin/env python
#-*-coding: latin1-*-
'''
Created on 14/11/2011

@author: Grupo Sistema Academico
'''
from db import db
class Professor:
    '''Classe de Gerenciamento de Professor'''
    def __init__(self, ide = None):
        '''Retorna Id do Professor'''
        self.__DataBase = db()
        if ide is None:
            self.__id = None # INT
            self.__dadosId = None # STR
            self.__loginId = None # STR
        else:
            self.carregar(ide)
            self.setId(ide)
    
    def getId(self):
        '''Retorna Dados do Professor'''
        return self.__id
    def setId(self, novoId):
        '''Edita Id do Professor'''
        self.__id = novoId
    
    def getDadosId(self):
        '''Retorna Login Id do Professor'''
        return self.__dadosId
    def setDadosId(self, novoDadosId):
        '''Edita Dados do Professor'''
        self.__dadosId = novoDadosId
    
    def getLoginId(self):
        '''Salva alterações no Banco de Dados'''
        return self.__loginId
    def setLoginId(self, novoLoginId):
        '''Edita Login Id do Professor'''
        self.__loginId = novoLoginId

    def carregar(self, ide):
        """Carrega professor a partir de id no BD"""
        self.__dados = self.__DataBase.carregarProfessor(ide)
        if self.__dados == None:
            return False
        else:
            self.setId(self.__dados[0])
            self.setDadosId(self.__dados[1])
            self.setLoginId(self.__dados[2])
            return True
        
    def salvarEdit(self, ide):
        """Salva ajuste de hora no BD"""
        return self.__DataBase.editarProfessor(ide, self.getDadosId(), self.getLoginId())

    def addNovo(self):
        """Cria um novo endereco no BD"""
        return self.__DataBase.addProfessor(self.getDadosId(), self.getLoginId())

    def delete(self, ide):
        """Deleta um professor a partir da ID"""
        return self.__DataBase.delProfessor(ide)

    def pegarId(self):
        """Retorna uma lista com todas as IDs de professores"""
        return self.__DataBase.returnIdProfessor()

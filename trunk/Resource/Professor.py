#!/usr/bin/env python
#-*-coding: latin1-*-
'''
Created on 14/11/2011

@author: Grupo Sistema Academico
'''
class Professor:
    '''Classe de Gerenciamento de Professor'''
    def __init__(self):
        self.__id = None # INT
        self.__dadosId = None # STR
        self.__loginId = None # STR
    '''Retorna Id do Professor'''
    def getId(self):
        return self.__id
    '''Edita Id do Professor'''
    def setId(self, novoId):
        return 0
    '''Retorna Dados do Professor'''
    def getDadosId(self):
        return self.__dadosId
    '''Edita Dados do Professor'''
    def setDadosId(self, novoDadosId):
        return 0
    '''Retorna Login Id do Professor'''
    def getLoginId(self):
        return self.__loginId
    '''Edita Login Id do Professor'''
    def setLoginId(self, novoLoginId):
        return 0
    '''Salva alterações no Banco de Dados'''
    def salvarEdit(self, id):
        return True #Retorna True ou False
    '''Carrega Informações do professor atraves do Banco de Dados'''
    def carregar(self, id):
        return True #Retorna True ou False
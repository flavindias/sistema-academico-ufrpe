#!/usr/bin/env python
#-*-coding: latin1-*-
'''
Created on 15/11/2011

@author: Grupo Sistema Academico
'''
class Responsavel:
    '''Classe para Gerenciamento de Conta do Responsavel'''
    def __init__(self):
        self.__id = None # INT
        self.__dadosId = None # STR
        self.__loginId = None # STR
    '''Retorna Id'''
    def getId(self):
        return self.__id
    '''Edita Id'''
    def setId(self, novoId):
        self.__id = novoId
        return 0
    '''Retorna dadosId'''
    def getDadosId(self):
        return self.__dadosId
    '''Edita dadosId'''
    def setDadosId(self, novoDadosId):
        self.__dadosId = novoDadosId
        return 0
    '''Retorna Id do Login'''
    def getLoginId(self):
        return self.__loginId
    '''Edita Id do Login'''
    def setLoginId(self, novoLoginId):
        self.__loginId = novoLoginId
        return 0
    '''Salva alterações no banco de dados'''
    def salvarEdit(self, id):
        return True #Retorna True ou False
    '''Carrega as informações de acordo com o id informado atraves do banco de dados'''
    def carregar(self, id):
        return True #Retorna True ou False
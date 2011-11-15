#!/usr/bin/env python
#-*-coding: latin1-*-
'''
Created on 15/11/2011

@author: Grupo Sistema Academico
'''
class Aluno:
    '''Classe de Gerenciamento de Aluno'''
    def __init__(self):
        self.__matricula = None # STR
        self.__dadosId = None # STR
        self.__situacao = None # STR
        self.__loginId = None # STR
        self.__turmaId = None # INT
    '''Retorna Número de Matricula do Aluno'''
    def getMatricula(self):
        return self.__matricula
    '''Edita Número de Matricula do Aluno'''
    def setMatricula(self, novaMatricula):
        self.__matricula = novaMatricula
        return 0
    '''Retorna DadosId do Aluno'''
    def getDadosId(self):
        return self.__dadosId
    '''Edita DadosId do Aluno'''
    def setDadosId(self, novoDadosId):
        self.__dadosId = novoDadosId
        return 0
    '''Retorna Situação do Aluno'''
    def getSituacao(self):
        return self.__situacao
    '''Edita Situação do Aluno'''
    def setSituacao(self, novaSituacao):
        self.__situacao = novaSituacao
        return 0
    '''Retorna LoginId do Aluno'''
    def getLoginId(self):
        return self.__loginId
    '''Edita LoginId do Aluno'''
    def setLoginId(self, novoLoginId):
        self.__loginId = novoLoginId
        return 0
    '''Retorna TurmaId do Aluno'''
    def getTurmaId(self):
        return self.__turmaId
    '''Edita TurmaId do Aluno'''
    def setTurmaId(self, novoTurmaId):
        self.__turmaId = novoTurmaId
        return 0
    '''Salva alterações no banco de dados'''
    def salvarEdit(self, id):
        return True #Retorna True ou False
    '''Carrega Informações atraves do Banco de dados'''
    def carregar(self, id):
        return True #Retorna True ou False
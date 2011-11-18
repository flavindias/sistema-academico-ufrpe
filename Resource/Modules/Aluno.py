#!/usr/bin/env python
#-*-coding: latin1-*-
'''
Created on 15/11/2011

@author: Grupo Sistema Academico
'''

import db

class Aluno:
    '''Classe de Gerenciamento de Aluno'''
    def __init__(self):
        """Classe para gerenciar alunos"""
        self.__matricula = None # INT LEN(6)
        self.__dadosId = None # STR
        self.__situacao = None # STR LEN(3) *apr = aprovado, rep = reprovado, ndf = nao definido, rec = recuperacao*
        self.__loginId = None # STR
        self.__turmaId = None # INT
        
    def getMatricula(self):
        '''Retorna Número de Matricula do Aluno'''
        return self.__matricula
    def setMatricula(self, novaMatricula):
        '''Ajusta DadosId do Aluno'''
        self.__matricula = novaMatricula
    
    def getDadosId(self):
        '''Retorna Situação do Aluno'''
        return self.__dadosId
    def setDadosId(self, novoDadosId):
        '''Edita DadosId do Aluno'''
        self.__dadosId = novoDadosId

    def getSituacao(self):
        '''Retorna Situação do Aluno'''
        return self.__situacao
    def setSituacao(self, novaSituacao):
        '''Retorna LoginId do Aluno'''
        self.__situacao = novaSituacao

    def getLoginId(self):
        '''Retorna LoginId do Aluno'''
        return self.__loginId
    def setLoginId(self, novoLoginId):
        '''Ajusta TurmaId do Aluno'''
        self.__loginId = novoLoginId
    
    def getTurmaId(self):
        '''Retorna turmaId do Aluno'''
        return self.__turmaId
    def setTurmaId(self, novoTurmaId):
        '''Edita TurmaId do Aluno'''
        self.__turmaId = novoTurmaId
        
    def salvarEdit(self):
        '''Altera informacoes atuais do Banco de dados'''
        return True #Retorna True ou False
    def carregar(self, matricula):
        '''Carrega informacoes do Banco de Dados'''
        return True #Retorna True ou False

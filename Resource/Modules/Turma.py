#!/usr/bin/env python
#-*-coding: latin1-*-
'''
Created on 14/11/2011

@author: Grupo Sistema Academico
'''
from db import db

class Turma:
    '''Classe de Gerenciamento de Turma'''
    def __init__(self, ide = None):
    """Inicia uma instancia no BD"""
        self.__DataBase = db()
        if ide is None:
            self.setId(None)
            self.setAno(None)
            self.setTurno(None)
            self.setDisc([])
        self.__id = None # INT
        self.__ano = None # INT
        self.__turno = None # STR
        self.__discId = [] # [INT]
    
    def getId(self):
        '''Retorna o Id da Turma'''
        return self.__id
    def setId(self, novoId):
        '''Edita o Id da Turma'''
        self.__id = novoId
    
    def getAno(self):
        '''Retorna o Ano da Turma'''
        return self.__ano
    def setAno(self, novoAno):
        '''Edita o Ano da Turma'''
        self.__ano = novoAno
        return 0
    
    def getTurno(self):
        '''Retorna o Turno da Turma'''
        return self.__turno
    def setTurno(self, novoTurno):
        '''Edita o Turno da Turma'''
        self.__turno = novoTurno
        return 0
    
    def getDisc(self, ide):
        '''Retorna a lista de Disciplinas da Turma'''
        return self.__discId
    def setDisc(self, pos, novoDisc):
        '''Adiciona Disciplina a Turma'''
        self.__discId[pos] += [novoDisc]
        return 0
    def excluirDisc(self, id):
        ''' Exclui Disciplina da Turma'''
        if id in self.__discId:
            self.__discId.remove(id)
            return True
        else:
            return False
    
    def salvarEdit(self, id):
        '''Salva alterações no Banco de Dados'''
        return True #Retorna True ou False
    
    def carregar(self, id):
        '''Carrega Informações da Turma atraves do Banco de Dados'''
        return True #Retorna True ou False

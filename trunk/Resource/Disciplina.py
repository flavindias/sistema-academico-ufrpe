#!/usr/bin/env python
#-*-coding: latin1-*-
'''
Created on 14/11/2011

@author: Grupo Sistema Academico
'''
class Disciplina:
    '''Classe de gerenciamento de Disciplinas'''
    def __init__(self):
        self.__id = None # INT
        self.__nome = None # STR
        self.__professorId = None # STR
    '''Retorna o  Id da Disciplina'''
    def getId(self):
        return self.__id
    '''Editar Id da Disciplina'''
    def setId(self, novoId):
        return 0
    '''Retorna Nome da Disciplina'''
    def getNome(self):
        return self.__nome
    '''Editar Nome da Disciplina'''
    def setNome(self, novoNome):
        return 0
    '''Retorna Id do Professor da Disciplina'''
    def getProfessorId(self):
        return self.__professorId
    '''Editar Id do Professor da Disciplina'''
    def setProfessorId(self, novoProfessorId):
        return 0
    '''Salvar alterações'''
    def salvarEdit(self, id):
        return True #Retorna True ou False
    '''Carregar Informações da Disciplina'''
    def carregar(self, id):
        return True #Retorna True ou False
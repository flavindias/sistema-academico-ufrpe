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
    '''Edita Id da Disciplina'''
    def setId(self, novoId):
        self.__id = novoId
        return 0
    '''Retorna Nome da Disciplina'''
    def getNome(self):
        return self.__nome
    '''Edita Nome da Disciplina'''
    def setNome(self, novoNome):
        self.__nome = novoNome
        return 0
    '''Retorna Id do Professor da Disciplina'''
    def getProfessorId(self):
        return self.__professorId
    '''Edita Id do Professor da Disciplina'''
    def setProfessorId(self, novoProfessorId):
        self.__professorId = novoProfessorId
        return 0
    '''Salva alterações no Banco de Dados'''
    def salvarEdit(self, id):
        return True #Retorna True ou False
    '''Carrega Informações da Disciplina atraves do Banco de Dados'''
    def carregar(self, id):
        return True #Retorna True ou False
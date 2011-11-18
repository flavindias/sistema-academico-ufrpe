#!/usr/bin/env python
#-*-coding: latin1-*-
'''
Created on 14/11/2011

@author: Grupo Sistema Academico
'''

from db import db

class Disciplina:
    '''Classe de gerenciamento de Disciplinas'''
    def __init__(self, ide = None):
        self.__DataBase = db()
        if ide is None:
            self.setId(None)
            self.setNome(None)
            self.setProfessorId(None)
        else:
            self.carregar(ide)
            self.setId(ide)
    
    def getId(self):
        '''Retorna o  Id da Disciplina'''
        return self.__id
    def setId(self, novoId):
        '''Edita Id da Disciplina'''
        self.__id = novoId
    
    def getNome(self):
        '''Retorna Nome da Disciplina'''
        return self.__nome
    def setNome(self, novoNome):
        '''Edita Nome da Disciplina'''
        self.__nome = novoNome
    
    def getProfessorId(self):
        '''Retorna Id do Professor da Disciplina'''
        return self.__professorId
    def setProfessorId(self, novoProfessorId):
        '''Edita Id do Professor da Disciplina'''
        self.__professorId = novoProfessorId

    def carregar(self, ide):
        """Carrega Informações da Disciplina atraves do Banco de Dados"""
        self.__dados = self.__DataBase.carregarDisciplina(ide)
        if self.__dados == None:
            return False
        else:
            self.setId(ide)
            self.setNome(self.__dados[1])
            self.setProfessorId(self.__dados[2])

    def salvarEdit(self, ide):
        """Salva alterações no Banco de Dados"""
        return self.__DataBase.editarDisciplina(ide, self.getNome(), self.getProfessorId())

    def addNova(self):
        """Cria uma nova linha no BD"""
        return self.__DataBase.addDisciplina(self.getNome(), self.getProfessorId())
    
    def delete(self, ide):
        """Deleta uma disciplina"""
        return self.__DataBase.delDisciplina(ide)

    def pegarId(self):
        """Retorna uma lista com todas as disciplinas"""
        return self.__DataBase.returnIdDisciplina()

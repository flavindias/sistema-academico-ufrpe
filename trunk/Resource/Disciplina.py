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

    def addNova(self):
        """Cria uma nova linha no BD"""
        return DataBase.addDisciplina(self.getNome(), self.getProfessorId())
    
    def salvarEdit(self, ide):
        """Salva alterações no Banco de Dados"""
        return DataBase.editarDisciplina(ide, self.getNome(), self.getProfessorId())
    
    def carregar(self, ide):
        """Carrega Informações da Disciplina atraves do Banco de Dados"""
        self.__dados = DataBase.carregarDisciplina(ide)
        if self.__dados == None:
            return False
        else:
            self.setId(ide)
            self.setNome(self.__dados[1])
            self.setProfessorId(self.__dados[2])

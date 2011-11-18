#!/usr/bin/env python
#-*-coding: latin1-*-
'''
Created on 14/11/2011

@author: Grupo Sistema Academico
'''
class Turma:
    '''Classe de Gerenciamento de Turma'''
    def __init__(self):
        self.__id = None # INT
        self.__ano = None # INT
        self.__turno = None # STR
        self.__discId = [] # [INT]
    '''Retorna o Id da Turma'''
    def getId(self):
        return self.__id
    '''Edita o Id da Turma'''
    def setId(self, novoId):
        self.__id = novoId
        return 0
    '''Retorna o Ano da Turma'''
    def getAno(self):
        return self.__ano
    '''Edita o Ano da Turma'''
    def setAno(self, novoAno):
        self.__ano = novoAno
        return 0
    '''Retorna o Turno da Turma'''
    def getTurno(self):
        return self.__turno
    '''Edita o Turno da Turma'''
    def setTurno(self, novoTurno):
        self.__turno = novoTurno
        return 0
    '''(Em Edição) - Retorna a Disciplina da Turma'''
    def getDisc(self, id):
        return True
    '''Adiciona Disciplina a Turma'''
    def setDisc(self, novoDisc):
        self.__discId += [novoDisc]
        return 0
    ''' Exclui Disciplina da Turma'''
    def excluirDisc(self, id):
        if id in self.__discId:
            self.__discId.remove(id)
            return True
        else:
            return False
    '''Salva alterações no Banco de Dados'''
    def salvarEdit(self, id):
        return True #Retorna True ou False
    '''Carrega Informações da Turma atraves do Banco de Dados'''
    def carregar(self, id):
        return True #Retorna True ou False
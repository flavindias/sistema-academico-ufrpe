#!/usr/bin/env python
#-*-coding: latin1-*-
'''
Created on 15/11/2011

@author: Grupo Sistema Academico
'''
class Nota:
    '''Classe de gerenciamento de Notas'''
    def __init__(self):
        self.__id = None # INT
        self.__disciplinaId = None # INT
        self.__alunoId = None # STR
        self.__unidade = None # INT
        self.__valor = None # FLOAT
    '''Retorna Id da Nota'''
    def getId(self):
        return self.__id
    '''Edita Id da Nota'''
    def setId(self, novoId):
        self.__id = novoId
        return 0
    '''Retorna DisciplinaId da Nota'''
    def getDisciplinaId(self):
        return self.__disciplinaId
    '''Edita DisciplinaId da Nota'''
    def setDisciplinaId(self, novoDisciplinaId):
        self.__disciplinaId = novoDisciplinaId
        return 0
    '''Retorna AlunoId da Nota'''
    def getAlunoId(self):
        return self.__alunoId
    '''Edita AlunoId da Nota'''
    def setAlunoId(self, novoAlunoId):
        self.__alunoId = novoAlunoId
        return 0
    '''Retorna a Unidade da Nota'''
    def getUnidade(self):
        return self.__unidade
    '''Edita a Unidade da Nota'''
    def setUnidade(self, novoUnidade):
        self.__unidade = novoUnidade
        return 0
    '''Retorna o Valor da Nota'''
    def getValor(self):
        return self.__valor
    '''Edita o Valor da Nota'''
    def setValor(self, novoValor):
        self.__valor = novoValor
        return 0
    '''Salva alterações no banco de dados'''
    def salvarEdit(self, id):
        return True #Retorna True ou False
    '''Carrega as informações atraves do banco de dados'''
    def carregar(self, id):
        return True #Retorna True ou False
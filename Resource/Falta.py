#!/usr/bin/env python
#-*-coding: latin1-*-
'''
Created on 15/11/2011

@author: Grupo Sistema Academico
'''
class Falta:
    '''Classe para Gerenciamento de Faltas'''
    def __init__(self):
        self.__id = None # INT
        self.__disciplinaId = None # INT
        self.__alunoId = None # STR
        self.__unidade = None # INT
        self.__qtde = None # INT
    '''Retorna Id'''
    def getId(self):
        return self.__id
    '''Edita Id'''
    def setId(self, novoId):
        self.__id = novoId
        return 0
    '''Retorna o Id da Disciplina que a Falta foi aplicada'''
    def getDisciplinaId(self):
        return self.__disciplinaId
    '''Edita o Id da Disciplina que a Falta foi aplicada'''
    def setDisciplinaId(self, novoDisciplinaId):
        self.__disciplinaId = novoDisciplinaId
        return 0
    '''Retorna o Id do Aluno que a Falta foi aplicada'''
    def getAlunoId(self):
        return self.__alunoId
    '''Edita o Id do Aluno que a Falta foi aplicada'''
    def setAlunoId(self, novoAlunoId):
        self.__alunoId = novoAlunoId
        return 0
    '''Retorna a Unidade que a Falta foi aplicada'''
    def getUnidade(self):
        return self.__unidade
    '''Edita a Unidade que a Falta foi aplicada'''
    def setUnidade(self, novoUnidade):
        self.__unidade = novoUnidade
        return 0
    '''Retorna a Quantidade de Faltas'''
    def getQtde(self):
        return self.__qtde
    '''Edita a Quantidade de Faltas'''
    def setQtde(self, novoQtde):
        self.__qtde = novoQtde
        return 0
    '''Salva as alterações no banco de dados'''
    def salvarEdit(self, id):
        return True #Retorna True ou False
    '''Carrega as informações do id informado atraves do banco de dados'''
    def carregar(self, id):
        return True #Retorna True ou False
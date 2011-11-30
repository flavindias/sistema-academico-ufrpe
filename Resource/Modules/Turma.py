#!/usr/bin/env python
#-*-coding: latin1-*-
"""
Created on 14/11/2011

@author: Grupo Sistema Academico
"""
from db import db

class Turma:
    """Classe de Gerenciamento de Turma"""
    def __init__(self, ide = None):
        """Inicia uma instancia no BD"""
        self.__DataBase = db()
        if ide is None:
            self.setId(None)
            self.setAno(None)
            self.setTurno(None)
            self.setDisc([])
        else:
            self.carregar(ide)
            self.setId(ide)

    def getId(self):
        """Retorna o Id da Turma"""
        return self.__id
    def setId(self, novoId):
        """Edita o Id da Turma"""
        self.__id = novoId

    def getAno(self):
        """Retorna o Ano da Turma"""
        return self.__ano
    def setAno(self, novoAno):
        """Edita o Ano da Turma"""
        self.__ano = novoAno

    def getTurno(self):
        """Retorna o Turno da Turma"""
        return self.__turno
    def setTurno(self, novoTurno):
        """Edita o Turno da Turma"""
        self.__turno = novoTurno

    def getDisc(self):
        """Retorna a lista de Disciplinas da Turma"""
        return self.__disc
    def setDisc(self, novoDisc):
        """Adiciona Disciplina a Turma"""
        self.__disc = novoDisc

    def carregar(self, ide):
        """Carrega Informações da Turma atraves do Banco de Dados"""
        self.__dados = self.__DataBase.carregarTurma(ide)
        if self.__dados == None:
            return False
        else:
            self.setId(ide)
            self.setAno(self.__dados[1])
            self.setTurno(self.__dados[2])
            self.__list = []
            for self.__i in range (3, 10):
                self.__list.append(self.__dados[self.__i])
            self.setDiscI(self.__list)

    def addNova(self):
        """Cria uma nova Turma no Banco de Dados"""
        return self.__DataBase.addTurma(self.getAno(), self.getTurno(), self.getDisc())

    def salvarEdit(self, id):
        """Salva alterações no Banco de Dados"""
        return self.__DataBase.editarTurma(ide, ano = self.getAno(), turno = self.getTurno(), disc = self.getDisc())

    def delete(self, ide):
        """Deleta uma Turma"""
        return self.__DataBase.delTurma(ide)

    def pegarId(self):
        """Retorna uma lista com todas as Turmas"""
        return self.__DataBase.returnIdTurma()
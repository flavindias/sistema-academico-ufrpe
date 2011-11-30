#!/usr/bin/env python
#-*-coding: latin1-*-
"""
Created on 15/11/2011

@author: Grupo Sistema Academico
"""

import db

class Aluno:
    """Classe de Gerenciamento de Aluno"""
    def __init__(self, matricula = None):
        """Classe para gerenciar alunos"""
        self.__DataBase = db()
        if matricula is None:
            self.setMatricula(None) # INT
            self.setDadosId(None) # STR
            self.setSituacaocao(None) # STR LEN(3) *apr = aprovado, rep = reprovado, ndf = nao definido, rec = recuperacao*
            self.setLoginId(None) # STR
            self.setTurmaId(None) # INT
        else:
            self.carregar(matricula)
            self.setMatricula(matricula)

    def getMatricula(self):
        """Retorna Número de Matricula do Aluno"""
        return self.__matricula
    def setMatricula(self, novaMatricula):
        """Ajusta DadosId do Aluno"""
        self.__matricula = novaMatricula

    def getDadosId(self):
        """Retorna Situação do Aluno"""
        return self.__dadosId
    def setDadosId(self, novoDadosId):
        """Edita DadosId do Aluno"""
        self.__dadosId = novoDadosId

    def getSituacao(self):
        """Retorna Situação do Aluno"""
        return self.__situacao
    def setSituacao(self, novaSituacao):
        """Retorna LoginId do Aluno"""
        self.__situacao = novaSituacao

    def getLoginId(self):
        """Retorna LoginId do Aluno"""
        return self.__loginId
    def setLoginId(self, novoLoginId):
        """Ajusta TurmaId do Aluno"""
        self.__loginId = novoLoginId

    def getTurmaId(self):
        """Retorna turmaId do Aluno"""
        return self.__turmaId
    def setTurmaId(self, novoTurmaId):
        """Edita TurmaId do Aluno"""
        self.__turmaId = novoTurmaId

    def carregar(self, ide):
        """Carrega aluno a partir de id no Banco de Dados"""
        self.__dados = self.__DataBase.carregarAluno(ide)
        if self.__dados == None:
            return False
        else:
            self.setMatricula(self.__dados[0])
            self.setDadosId(self.__dados[1])
            self.setSituacao(self.__dados[2])
            self.setLoginId(self.__dados[3])
            setTurmaId(self.__dados[4])
            return True

    def salvarEdit(self, matricula):
        """Salva ajuste de aluno no Banco de Dados"""
        return self.__DataBase.editarAluno(self.getMatricula(), self.getDadosId(), self.getSituacao(), self.getLoginId(), self.getTurmaId())

    def addNovo(self):
        """Cria um novo aluno no Banco de Dados"""
        return self.__DataBase.addAluno(self.getDadosId(), self.getSituacao(), self.getLoginId(), self.getTurmaId())

    def delete(self, matricula):
        """Deleta um aluno a partir da matricula"""
        return self.__DataBase.delAluno(matricula)

    def pegarId(self):
        """Retorna uma lista com todas as matriculas dos alunos"""
        return self.__DataBase.returnIdAluno()
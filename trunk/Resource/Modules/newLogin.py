#-------------------------------------------------------------------------------
# Name:        Login
# Purpose:     Classe de gerenciamento para instancias de login criadas
#
# Author:      Igor Mateus
#
# Created:     02/12/2011
# Copyright:   (c) AcademicSYS 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import DataBase

class Login:
    """Classe Login"""
    def setLogin(self, novoLogin):
        """Ajusta o Login"""
        self.__login=novoLogin
    def setSenha(self, novoSenha):
        """Ajusta a senha"""
        self.__senha=novoSenha
    def setTipo(self, novoTipo):
        """Ajusta o tipo"""
        self.__tipo=novoTipo
    def getLogin(self):
        """Retorna o login"""
        return self.__login
    def getSenha(self):
        """Retorna a senha"""
        return self.__senha
    def getTipo(self):
        """Retorna o tipo de login"""
        return self.__tipo

    def __init__(self, login=None):
        """Inicia uma instanca de login"""
        if login == None:
            self.setLogin(None) #str len 11
            self.setSenha(None) #str max len 30
            self.setTipo(None) #str len 3
        else:
            self.carregar(login)

    def carregar(self, login):
        """Carrega um login a partir do BD"""
        self.__result=DataBase.carregarLogin(login)
        if self.__result == None:
            return False
        else:
            self.setLogin(self.__result[0])
            self.setSenha(self.__result[1])
            self.setTipo(self.__result[2])
            return True

    def salvarEdit(self, login, senha=None, tipo=None):
        """Salva uma edicao de login no BD"""
        return DataBase.editarLogin(login, senha, tipo)

    def listaDb(self):
        """Retorna uma lista com todos os logins do BD"""
        return DataBase.getListDbLogin()

    def add(self, login, senha, tipo):
        """Adiciona um Login no BD"""
        return DataBase.addLogin(login, senha, tipo)

    def delete(self, login):
        """Deleta um Login do BD"""
        return DataBase.deleteLogin(login)

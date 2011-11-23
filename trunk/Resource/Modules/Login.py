'''
Created on 15/11/2011

@author: Grupo Sistema Academico
'''

from db import db
import base64

class Login:
    """Classe para gerenciamento de logins"""
    def __init__(self, ide = None):
        """Inicia nova instancia login carregando ou nao"""
        self.__DataBase = db()
        if ide == None:
            self.setUsuario(None)
            self.setSenha(None)
            self.setTipo(None)
        else:
            self.carregar(ide)

    def getUsuario(self):
        """Retorna o usuario"""
        return self.__usuario
    def setUsuario(self, novoUsuario):
        """Ajusta o usuario"""
        self.__usuario = novoUsuario
        
    def getTipo(self):
        """Retorna o tipo do usuario"""
        return self.__tipo
    def setTipo(self, novoTipo):
        """Ajusta o tipo de um usuario"""
        self.__tipo = novoTipo
        
    def getSenha(self):
        """Retorna a senha"""
        return self.decript(self.__senha)
    def setSenha(self, novoSenha):
        """Ajusta a senha"""
        if novoSenha is not None:
            self.__senha = self.cript(novoSenha)

    def cript(self, senha):
        """Criptografa uma senha"""
        try:
            return base64.b64encode(senha)
        except:
            return None
    def decript(self, senha):
        """Descriptografa uma senha"""
        try:
            return base64.b64decode(senha)
        except:
            return None

    def carregar(self, usuarioId):
        """Carrega informacoes a partir de uma id"""
        self.__dados = self.__DataBase.carregarLogin(usuarioId)
        if self.__dados == None:
            return False
        else:
            self.setUsuario(self.__dados[0])
            self.setSenha(self.__dados[1])
            self.setTipo(self.__dados[2])
            return True

    def salvarEdit(self, usuarioId):
        """Salva uma edicao"""
        return self.__DataBase.editarLogin(usuarioID, usuario = self.getUsuario(), senha = self.cript(self.getSenha()), tipo = self.getTipo())

    def addNova(self):
        """Adiciona um novo usuario ao banco de dados"""
        if self.getUsuario() is not None and self.getSenha() is not None and self.getTipo() is not None:
            return self.__DataBase.addLogin(self.getUsuario(), self.cript(self.getSenha()), self.getTipo())
        return False

    def delete(self, usuario):
        """Deleta um usuario"""
        return self.__DataBase.delLogin(usuario)

    def pegarId(self):
        """Retorna todas as Ids de Login"""
        return self.__DataBase.returnIdLogin()
        
    def valida(self, usuario, senha):
        """Valida usuario e senha pelo Banco de dados"""
        return self.__DataBase.validarLogin(usuario, self.cript(senha))

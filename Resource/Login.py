import base64

class Log:
    """Classe que gerencia os usuarios"""

    def __init__(self, usuario, senha, tipo = 'aluno'):
        """Inicia um novo Usuario"""
        self.__usuario = usuario
        self.__senha = base64.b64encode(senha)
        self.__nivel = tipo

    def getUsuario(self):
        """Retorna o Usuario"""
        return self.__usuario
    def setUsuario(self, novoUsuario):
        """Edita o nome do usuario"""
        self.__usuario = novoUsuario

    def getSenha(self):
        """Retorna a Senha"""
        return base64.b64decode(self.__senha)
    def setSenha(self, novaSenha):
        """Edita a senha"""
        self.__senha = base64.b64encode(novaSenha)

    def getNivel(self):
        """Retorna o nivel de acesso"""
        return self.__nivel
    def setLevel(self, novoNivel):
        """Edita o nivel de acesso"""
        self.__nivel = novoNivel

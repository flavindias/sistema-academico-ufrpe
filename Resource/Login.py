import base64

class Log:
    """Classe que gerencia os usuarios"""

    def __init__(self, user, password, tipo):
        """Inicia um novo Usuario"""
        self.__user = user
        self.__password = base64.b64encode(password)
        self.__level = tipo

    def getUser(self):
        """Retorna o Usuario"""
        return self.__user
    def setUser(self, newUser):
        """Edita o nome do usuario"""
        self.__user = newUser

    def getPassword(self):
        """Retorna a Senha"""
        return self.__password
    def setPassword(self, newWord):
        """Edita a senha"""
        self.__password = newWord

    def getLevel(self):
        """Retorna o nivel de acesso"""
        return self.__level
    def setLevel(self, newLevel):
        """Edita o nivel de acesso"""
        self.__level = newLevel

import MySQLdb

class db:
    """Classe gerente de banco de dados"""
    def __init__(self):
        """Inicia conexao ao banco de dados"""
        self.connection = MySQLdb.connect(host="db4free.net", db="academicsys", user="desenvolvedores", passwd="acesso")
        self.cursor = self.connection.cursor()

    #***AREA DE COMUNICACAO COM A CLASSE DATA***
    def carregarData(self, ide):
        """Carrega uma data apardir da ID"""
        self.__id = str(ide)
        self.cursor.execute("SELECT * FROM DATAS WHERE ID = %s;", (self.__id))
        if self.cursor.rowcount == 1:
            return self.cursor.fetchone()
        else:
            return None

    def editarData(self, ide, ano, mes, dia, hora = None):
        """Salva um ajuste efetuado na data"""
        try:
            if ide == None:
                return False
            else:
                self.__temp = str(ano)+'-'+str(mes)+'-'+str(dia)
                self.cursor.execute("UPDATE DATAS SET DAT = '%s' WHERE ID = %d;" %(self.__temp, ide))
                if hora == None:
                    self.cursor.execute("UPDATE DATAS SET HORA = '%s' WHERE ID = %d;" %(hora, ide))
                return True
        except:
            return False

    def addData(self, ano, mes, dia, hora = None):
        """Cria uma nova data"""
        try:
            self.__temp = str(ano)+'-'+str(mes)+'-'+str(dia)
            if hora == None:
                self.cursor.execute("INSERT INTO DATAS(ID, DAT, HORA) VALUES (NULL, %s, NULL);" %(self.__temp))
                return True
            else:
                self.cursor.execute("INSERT INTO DATAS(ID, DAT, HORA) VALUES (NULL, %s, %s);" %(self.__temp, hora))
                return True
        except:
            return False

    #***AREA DE COMUNICACAO COM A CLASSE ENDERECO***
    def carregarLogin(self, loginId):
        """Carrega uma usuario apardir da ID"""
        self.__id = str(loginId)
        self.cursor.execute("SELECT * FROM LOGIN WHERE USUARIO = %s;", (self.__id))
        if self.cursor.rowcount == 1:
            return self.cursor.fetchone()
        else:
            return None

    def editarLogin(self, ide, usuario = None, senha = None, tipo = None):
        """Salva um ajuste efetuado na data"""
        try:
            if ide is None:
                return False
            else:
                if usuario != None:
                    self.cursor.execute("UPDATE LOGIN SET USUARIO = '%s' WHERE ID = %d;" %(usuario, ide))
                if senha != None:
                    self.cursor.execute("UPDATE LOGIN SET SENHA = '%s' WHERE ID = %d;" %(senha, ide))
                if tipo != None:
                    self.cursor.execute("UPDATE LOGIN SET TIPO = '%s' WHERE ID = %d;" %(tipo, ide))
                return True
        except:
            return False

    def validarLogin(self, usuario, senha):
        """Retorna bool para uma validacao"""
        if usuario is not None and senha is not None:
            cursor.execute("SELECT SENHA FROM LOGIN WHERE USUARIO = %s;" %(usuario))
            self.__temp = cursor.fetchone()
            if self.__temp is not None and self.__temp[0] is senha:
                return True
        return False

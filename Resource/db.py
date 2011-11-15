import MySQLdb

class db:
    """Classe gerente de banco de dados"""
    def __init__(self):
        """Inicia conexao ao banco de dados"""
        self.connection = MySQLdb.connect(host="db4free.net", db="academicsys", user="desenvolvedores", passwd="acesso")
        self.cursor = self.connection.cursor()

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

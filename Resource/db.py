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
                self.cursor.execute("UPDATE DATAS SET DAT = '%s' WHERE ID = %s;" %(self.__temp, ide))
                if hora == None:
                    self.cursor.execute("UPDATE DATAS SET HORA = '%s' WHERE ID = %s;" %(hora, ide))
                return True
        except:
            return False

    def addData(self, ano, mes, dia, hora = None):
        """Cria uma nova data"""
        try:
            self.__temp = str(ano)+'-'+str(mes)+'-'+str(dia)
            if hora == None:
                self.cursor.execute("INSERT INTO DATAS(ID, DAT, HORA) VALUES (NULL, '%s', NULL);" %(self.__temp))
                return True
            else:
                self.cursor.execute("INSERT INTO DATAS(ID, DAT, HORA) VALUES (NULL, '%s', '%s');" %(self.__temp, hora))
                return True
        except:
            return False

    #***AREA DE COMUNICACAO COM A CLASSE LOGIN***
    def carregarLogin(self, loginId):
        """Carrega uma usuario apardir da ID"""
        self.__id = str(loginId)
        self.cursor.execute("SELECT * FROM LOGIN WHERE USUARIO = '%s';", (self.__id))
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
                    self.cursor.execute("UPDATE LOGIN SET USUARIO = '%s' WHERE ID = %s;" %(usuario, ide))
                if senha != None:
                    self.cursor.execute("UPDATE LOGIN SET SENHA = '%s' WHERE ID = %s;" %(senha, ide))
                if tipo != None:
                    self.cursor.execute("UPDATE LOGIN SET TIPO = '%s' WHERE ID = %s;" %(tipo, ide))
                return True
        except:
            return False

    def validarLogin(self, usuario, senha):
        """Retorna bool para uma validacao"""
        if usuario is not None and senha is not None:
            cursor.execute("SELECT SENHA FROM LOGIN WHERE USUARIO = '%s';" %(usuario))
            self.__temp = cursor.fetchone()
            if self.__temp is not None and self.__temp[0] is senha:
                return True
        return False

    def addLogin(self, usuario, senha, tipo):
        """Cria um novo usuario"""
        try:
            self.cursor.execute("INSERT INTO LOGIN(USUARIO, SENHA, TIPO) VALUES ('%s', '%s', '%s');" %(usuario, senha, tipo))
            return True
        except:
            return False

    #***AREA DE COMUNICACAO COM A CLASSE ENDERECO***
    def carregarEndereco(self, ide):
        """Carrega uma endereco a partir da ID"""
        self.__id = int(ide)
        self.cursor.execute("SELECT * FROM ENDERECO WHERE ID = %s;", (self.__id))
        if self.cursor.rowcount == 1:
            return self.cursor.fetchone()
        else:
            return None

    def addEndereco(self, rua, num, bairro, cidade, uf, cep, complemento = None):
        """Cria um novo endereco no banco de dados"""
        try:
            if complemento is None:
                self.cursor.execute("INSERT INTO ENDERECO(ID, RUA, NUM, BAIRRO, CIDADE, UF, CEP, COMPLEMENTO) VALUES (NULL, '%s', %s, '%s', '%s', '%s', '%s', NULL);" %(rua, num, bairro, cidade, uf, cep))
                return True
            else:
                self.cursor.execute("INSERT INTO ENDERECO(ID, RUA, NUM, BAIRRO, CIDADE, UF, CEP, COMPLEMENTO) VALUES (NULL, '%s', %s, '%s', '%s', '%s', '%s', '%s');" %(rua, num, bairro, cidade, uf, cep, complemento))
                return True
        except:
            return False

    def editarEndereco(self, ide, rua = None, num = None, bairro = None, cidade = None, uf = None, cep = None, complemento = None):
        """Salva um ajuste efetuado na endereco"""
        try:
            if ide is None:
                return False
            else:
                if rua != None:
                    self.cursor.execute("UPDATE ENDERECO SET RUA = '%s' WHERE ID = %s;" %(rua, ide))
                if num != None:
                    self.cursor.execute("UPDATE ENDERECO SET NUM = %s WHERE ID = %s;" %(num, ide))
                if bairro != None:
                    self.cursor.execute("UPDATE ENDERECO SET BAIRRO = '%s' WHERE ID = %s;" %(bairro, ide))
                if cidade != None:
                    self.cursor.execute("UPDATE ENDERECO SET CIDADE = '%s' WHERE ID = %s;" %(cidade, ide))
                if uf != None:
                    self.cursor.execute("UPDATE ENDERECO SET UF = '%s' WHERE ID = %s;" %(uf, ide))
                if cep != None:
                    self.cursor.execute("UPDATE ENDERECO SET CEP = '%s' WHERE ID = %s;" %(cep, ide))
                if complemento != None:
                    self.cursor.execute("UPDATE ENDERECO SET COMPLEMENTO = '%s' WHERE ID = %s;" %(complemento, ide))
                return True
        except:
            return False

    #***AREA DE COMUNICACAO COM A CLASSE PROFESSOR***
    def carregarProfessor(self, ide):
        """Carrega uma Professor a partir da ID"""
        self.__id = int(ide)
        self.cursor.execute("SELECT * FROM PROFESSOR WHERE ID = %s;", (self.__id))
        if self.cursor.rowcount == 1:
            return self.cursor.fetchone()
        else:
            return None

    def addProfessor(self, dadosId, loginId):
        """Cria um novo professor no banco de dados"""
        try:
            self.cursor.execute("INSERT INTO PROFESSOR(ID, DADOS, LOGIN) VALUES (NULL, '%s', '%s');" %(dadosId, loginId))
            return True
        except:
            return False

    def editarProfessor(self, ide, dadosId = None, loginId = None):
        """Salva um ajuste efetuado no professor"""
        try:
            if ide is None:
                return False
            else:
                if dadosId != None:
                    self.cursor.execute("UPDATE PROFESSOR SET DADOS = '%s' WHERE ID = %s;" %(dadosId, ide))
                if loginId != None:
                    self.cursor.execute("UPDATE PROFESSOR SET DADOS = '%s' WHERE ID = %s;" %(loginId, ide))
                return True
        except:
            return False

    #***AREA DE COMUNICACAO COM A CLASSE DADOSPESSOAIS***
    def carregarDadosPessoais(self, documento):
        """Carrega uma DadoPessoais a partir do documento"""
        self.__id = int(documento)
        self.cursor.execute("SELECT * FROM DADOS_PESSOAIS WHERE DOCUMENTO = '%s';", (self.__id))
        if self.cursor.rowcount == 1:
            return self.cursor.fetchone()
        else:
            return None

    def addDadosPessoais(self, documento, nome, sexo, dataNascId, enderecoId, celular = None, fixo = None):
        """Cria um novo endereco no banco de dados"""
        if sexo:
            sexo = 'TRUE'
        else:
            sexo = 'FALSE'
        try:
            self.cursor.execute("INSERT INTO DADOS_PESSOAIS(DOCUMENTO, NOME, SEXO, CELULAR, FIXO, DATA_NASC, ENDERECO) VALUES ('%s', '%s', %s, NULL, NULL, %s, %s);" %(documento, nome, sexo, dataNascId, enderecoId))
            if celular is not None:
                self.cursor.execute("UPDATE DADOS_PESSOAIS SET CELULAR = '%s' WHERE DOCUMENTO = '%s';" %(celular, documento))
            if fixo is not None:
                self.cursor.execute("UPDATE DADOS_PESSOAIS SET FIXO = '%s' WHERE DOCUMENTO = '%s';" %(fixo, documento))
            return True
        except:
            return False

    def editarDadosPessoais(self, documento = None, nome = None, sexo = None, dataNascId = None, enderecoId = None, celular = None, fixo = None):
        """Salva um ajuste efetuado na endereco"""
        try:
            if documento is None:
                return False
            else:
                if nome != None:
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET NOME = '%s' WHERE DOCUMENTO = '%s';" %(rua, ide))
                if sexo != None:
                    if sexo:
                        sexo = 'TRUE'
                    else:
                        sexo = 'FALSE'
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET SEXO = %s WHERE DOCUMENTO = '%s';" %(num, ide))
                if dataNascId != None:
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET DATA_NASC = %s WHERE DOCUMENTO = '%s';" %(bairro, ide))
                if enderecoId != None:
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET ENDERECO = %s WHERE DOCUMENTO = '%s';" %(cidade, ide))
                if celular != None:
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET CELULAR = '%s' WHERE DOCUMENTO = '%s';" %(uf, ide))
                if fixo != None:
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET FIXO = '%s' WHERE DOCUMENTO = '%s';" %(cep, ide))
                return True
        except:
            return False

import MySQLdb

class db:
    """Classe gerente de banco de dados"""
    def __init__(self):
        """Inicia conexao ao banco de dados"""
        self.connection = MySQLdb.connect(host="db4free.net", db="academicsys", user="desenvolvedores", passwd="acesso")
        self.cursor = self.connection.cursor()
        

    #***AREA DE COMUNICACAO COM A CLASSE DATA***
    def carregarData(self, ide):
        """Carrega uma data a partir da ID"""
        try:
            self.__id = str(ide)
            self.cursor.execute("SELECT * FROM DATAS WHERE ID = %s;", (self.__id))
            if self.cursor.rowcount == 1:
                return self.cursor.fetchone()
            else:
                return None
        except:
            return None

    def editarData(self, ide, ano, mes, dia, hora = None):
        """Salva um ajuste efetuado na data"""
        try:
            if ide == None:
                return False
            else:
                self.__temp = str(ano)+'-'+str(mes)+'-'+str(dia)
                self.cursor.execute("UPDATE DATAS SET DAT = '%s' WHERE ID = %s;" %(self.__temp, ide))
                if hora != None:
                    self.cursor.execute("UPDATE DATAS SET HORA = '%s' WHERE ID = %s;" %(hora, ide))
                if hora == None:
                    self.cursor.execute("UPDATE DATAS SET HORA = NULL WHERE ID = %s;" %(ide))
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

    def delData(self, ide = None):
        """Deleta uma das datas criadas"""
        try:
            if ide is not None:
                self.cursor.execute("DELETE FROM DATAS WHERE ID = %s;" %(ide))
                return True
            else:
                return False
        except:
            return False

    def returnIdData(self):
        """Retorna todas as IDs de data"""
        self.cursor.execute("SELECT ID FROM DATAS;")
        self.__result = self.cursor.fetchall()
        self.__lista = []
        try:
            for self.__i in self.__result:
                self.__lista.append(self.__i[0])
            return self.__lista
        except:
            return []
        

    #***AREA DE COMUNICACAO COM A CLASSE LOGIN***
    def carregarLogin(self, loginId):
        """Carrega uma usuario a partir do Usuario"""
        try:
            self.cursor.execute("SELECT * FROM LOGIN WHERE USUARIO = %s;", (loginId))
            if self.cursor.rowcount == 1:
                return self.cursor.fetchone()
            else:
                return None
        except:
            return None

    def editarLogin(self, loginId, senha = None, tipo = None):
        """Salva um ajuste efetuado no login"""
        try:
            if loginId is None:
                return False
            else:
                if senha != None:
                    self.cursor.execute("UPDATE LOGIN SET SENHA = '%s' WHERE USUARIO = '%s';" %(senha, loginId))
                if tipo != None:
                    self.cursor.execute("UPDATE LOGIN SET TIPO = '%s' WHERE USUARIO = '%s';" %(tipo, loginId))
                return True
        except:
            return False

    def addLogin(self, usuario, senha, tipo):
        """Cria um novo usuario"""
        try:
            self.cursor.execute("INSERT INTO LOGIN(USUARIO, SENHA, TIPO) VALUES ('%s', '%s', '%s');" %(usuario, senha, tipo))
            return True
        except:
            return False

    def delLogin(self, documento = None):
        """Deleta um login no BD"""
        try:
            if documento is not None:
                self.cursor.execute("DELETE FROM LOGIN WHERE USUARIO = '%s';" %(documento))
                return True
            else:
                return False
        except:
            return False

    def returnIdLogin(self):
        """Retorna os documentos de todos os logins cadastrados"""
        self.cursor.execute("SELECT USUARIO FROM LOGIN;")
        self.__result = self.cursor.fetchall()
        self.__lista = []
        try:
            for self.__i in self.__result:
                self.__lista.append(self.__i[0])
            return self.__lista
        except:
            return []
        
    def validarLogin(self, usuario, senha):
        """Retorna bool para uma validacao"""
        try:
            if usuario is not None and senha is not None:
                self.cursor.execute("SELECT SENHA FROM LOGIN WHERE USUARIO = '%s';" %(usuario))
                self.__temp = self.cursor.fetchone()
                if self.__temp[0] == senha:
                    return True
            return False
        except:
            return False
        

    #***AREA DE COMUNICACAO COM A CLASSE ENDERECO***
    def carregarEndereco(self, ide):
        """Carrega uma endereco a partir da ID"""
        try:
            self.__id = int(ide)
            self.cursor.execute("SELECT * FROM ENDERECO WHERE ID = %s;", (self.__id))
            if self.cursor.rowcount == 1:
                return self.cursor.fetchone()
            else:
                return None
        except:
            return None

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

    def delEndereco(self, ide):
        """Deleta um Endereco no BD a partir de uma ID"""
        try:
            if ide is not None:
                self.cursor.execute("DELETE FROM ENDERECO WHERE ID = %s;" %(ide))
                return True
        except:
            return False

    def returnIdEndereco(self):
        """Retorna uma lista com todas as IDs do endereco"""
        self.cursor.execute("SELECT ID FROM ENDERECO;")
        self.__result = self.cursor.fetchall()
        self.__lista = []
        try:
            for self.__i in self.__result:
                self.__lista.append(self.__i[0])
            return self.__lista
        except:
            return []
    

    #***AREA DE COMUNICACAO COM A CLASSE PROFESSOR***
    def carregarProfessor(self, ide):
        """Carrega uma Professor a partir da ID"""
        try:
            self.__id = int(ide)
            self.cursor.execute("SELECT * FROM PROFESSOR WHERE ID = %s;", (self.__id))
            if self.cursor.rowcount == 1:
                return self.cursor.fetchone()
            else:
                return None
        except:
            return None

    def editarProfessor(self, ide, dadosId = None, loginId = None):
        """Salva um ajuste efetuado no professor a partir da ID"""
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
        
    def addProfessor(self, dadosId, loginId):
        """Cria um novo professor no banco de dados"""
        try:
            self.cursor.execute("INSERT INTO PROFESSOR(ID, DADOS, LOGIN) VALUES (NULL, '%s', '%s');" %(dadosId, loginId))
            return True
        except:
            return False

    def delProfessor(self, ide):
        """Deleta um professor a partir da ID"""
        try:
            if ide is not None:
                self.cursor.execute("DELETE FROM PROFESSOR WHERE ID = %s;" %(ide))
                return True
        except:
            return False

    def returnIdProfessor(self):
        """Retorna uma lista de ID de professores"""
        self.cursor.execute("SELECT ID FROM PROFESSOR;")
        self.__result = self.cursor.fetchall()
        self.__lista = []
        try:
            for self.__i in self.__result:
                self.__lista.append(self.__i[0])
            return self.__lista
        except:
            return []

    def getProfByCpf(self, cpf):
        """Retorna o Id do professor pelo CPF"""
        self.cursor.execute("SELECT ID FROM PROFESSOR WHERE DADOS = '%s';")
        try:
            self.__result = self.cursor.fetchone()
            return self.__result
        except:
            return None


    #***AREA DE COMUNICACAO COM A CLASSE DADOSPESSOAIS***
    def carregarDadosPessoais(self, documento):
        """Carrega uma DadoPessoais a partir do documento"""
        self.__id = int(documento)
        self.cursor.execute("SELECT * FROM DADOS_PESSOAIS WHERE DOCUMENTO = %s;", (self.__id))
        if self.cursor.rowcount == 1:
            return self.cursor.fetchone()
        else:
            return None

    def editarDadosPessoais(self, documento = None, nome = None, sexo = None, dataNascId = None, enderecoId = None, celular = None, fixo = None):
        """Salva um ajuste efetuado na DadosPessoais a partir do Documento"""
        try:
            if documento is None:
                return False
            else:
                if nome != None:
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET NOME = '%s' WHERE DOCUMENTO = '%s';" %(nome, documento))
                if sexo != None:
                    if sexo == 1:
                        sexo = 'TRUE'
                    else:
                        sexo = 'FALSE'
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET SEXO = %s WHERE DOCUMENTO = '%s';" %(sexo, documento))
                if dataNascId != None:
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET DATA_NASC = %s WHERE DOCUMENTO = '%s';" %(dataNascId, documento))
                if enderecoId != None:
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET ENDERECO = %s WHERE DOCUMENTO = '%s';" %(enderecoId, documento))
                if celular != None:
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET CELULAR = '%s' WHERE DOCUMENTO = '%s';" %(celular, documento))
                if fixo != None:
                    self.cursor.execute("UPDATE DADOS_PESSOAIS SET FIXO = '%s' WHERE DOCUMENTO = '%s';" %(fixo, documento))
                return True
        except:
            return False

    def addDadosPessoais(self, documento, nome, sexo, dataNascId, enderecoId, celular = None, fixo = None):
        """Cria um novo endereco no banco de dados"""
        if sexo == 1:
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

    def delDadosPessoais(self, documento):
        """Deleta um dado pessoal a partir do documento"""
        try:
            if documento is not None:
                self.cursor.execute("DELETE FROM DADOS_PESSOAIS WHERE DOCUMENTO = '%s';" %(documento))
                return True
            else:
                return False
        except:
            return False

    def returnIdDadosPessoais(self):
        """Retorna uma lista de IDOCUMENTOS de todos os dados no BD"""
        self.cursor.execute("SELECT DOCUMENTO FROM DADOS_PESSOAIS;")
        self.__result = self.cursor.fetchall()
        self.__lista = []
        try:
            for self.__i in self.__result:
                self.__lista.append(self.__i[0])
            return self.__lista
        except:
            return []
    

    #***AREA DE COMUNICACAO COM A CLASSE DISCIPLINAS***
    def carregarDisciplina(self, ide):
        """Carrega uma disciplina a partir da ID"""
        self.__id = str(ide)
        self.cursor.execute("SELECT * FROM DISCIPLINA WHERE ID = %s;", (self.__id))
        if self.cursor.rowcount == 1:
            return self.cursor.fetchone()
        else:
            return None

    def editarDisciplina(self, ide, nome = None, professorId = None):
        """Salva um ajuste efetuado na disciplina"""
        try:
            if ide == None:
                return False
            else:
                if nome != None:
                    self.cursor.execute("UPDATE DISCIPLINA SET NOME = '%s' WHERE ID = %s;" %(nome, ide))
                if professorId != None:
                    self.cursor.execute("UPDATE DISCIPLINA SET PROFESSOR = %s WHERE ID = %s" %(professorId, ide))
                return True
        except:
            return False

    def addDisciplina(self, nome, professorId):
        """Cria uma nova disciplina"""
        try:
            if nome is not None and professorId is not None:
                self.cursor.execute("INSERT INTO DISCIPLINA(ID, NOME, PROFESSOR) VALUES (NULL, '%s', %s);" %(nome, professorId))
                return True
            else:
                return False
        except:
            return False

    def delDisciplina(self, ide):
        """Deleta uma disciplina do banco de dados"""
        try:
            if ide is not None:
                self.cursor.execute("DELETE FROM DISCIPLINA WHERE ID = %s;" %(ide))
                return True
            else:
                return False
        except:
            return False

    def returnIdDisciplina(self):
        """Retorna todas as ID de professores em lista"""
        self.cursor.execute("SELECT ID FROM DISCIPLINA ORDER BY NOME;")
        self.__result = self.cursor.fetchall()
        self.__lista = []
        try:
            for self.__i in self.__result:
                self.__lista.append(self.__i[0])
            return self.__lista
        except:
            return []

    #***AREA DE COMUNICACAO COM A CLASSE TURMA***
    def carregarTurma(self, ide):
        """Carrega uma turma a partir da ID"""
        self.__id = str(ide)
        self.cursor.execute("SELECT * FROM TURMA WHERE ID = %s;", (self.__id))
        if self.cursor.rowcount == 1:
            return self.cursor.fetchone()
        else:
            return None

    def editarTurma(self, ide, ano = None, turno = None, disc = []):
        """Salva um ajuste efetuado na Turma"""
        try:
            if ide == None:
                return False
            else:
                if ano != None:
                    self.cursor.execute("UPDATE TURMA SET ANO = %s WHERE ID = %s;" %(ano, ide))
                if turno != None
        except:
            return False

    def addTurma(self, nome, professorId):
        """Cria uma nova disciplina"""
        try:
            if nome is not None and professorId is not None:
                self.cursor.execute("INSERT INTO DISCIPLINA(ID, NOME, PROFESSOR) VALUES (NULL, '%s', %s);" %(nome, professorId))
                return True
            else:
                return False
        except:
            return False

    def delTurma(self, ide):
        """Deleta uma disciplina do banco de dados"""
        try:
            if ide is not None:
                self.cursor.execute("DELETE FROM DISCIPLINA WHERE ID = %s;" %(ide))
                return True
            else:
                return False
        except:
            return False

    def returnIdTurma(self):
        """Retorna todas as ID de professores em lista"""
        self.cursor.execute("SELECT ID FROM DISCIPLINA ORDER BY NOME;")
        self.__result = self.cursor.fetchall()
        self.__lista = []
        try:
            for self.__i in self.__result:
                self.__lista.append(self.__i[0])
            return self.__lista
        except:
            return []

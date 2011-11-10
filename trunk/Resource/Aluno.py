class Aluno:
    """Classe Aluno"""

    def __init__(self, nome, ano, turno, cpf, rg, sexo, dataNascimento, responsavel, email, telefone, endereco, login):
        """Cria um novo aluno"""
        self.__nome = nome
        self.__ano = ano
        self.__turno = turno
        self.__cpf = cpf
        self.__rg = rg
        self.__sexo = sexo
        self.__dataNasc = dataNascimento
        self.__responsavel = responsavel
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco
        self.__login = login

    def getNome(self):
        """Retorna o nome do aluno"""
        return self.__nome
    def setNome(self, novoNome):
        """Edita o nome do aluno"""
        self.__nome = novoNome
        
    def getAno(self):
        """Retorna o ano do aluno"""
        return self.__ano
    def setAno(self, novoAno):
        """Edita o ano do aluno"""
        self.__ano = novoAno
        
    def getTurno(self):
        """Retorna o turno do aluno"""
        return self.__turno
    def setTurno(self, novoTurno):
        """Edita o turno do aluno"""
        self.__turno = novoTurno
        
    def getCpf(self):
        """Retorna o CPF do aluno"""
        return self.__cpf
    def setCpf(self, novoCpf):
        """Edita o CPF do aluno"""
        self.__cpf = novoCpf

    def getRg(self):
        """Retorna o RG do aluno"""
        return self.__rg
    def setRg(self, novoRg):
        """Edita o RG do aluno"""
        self.__rg = novoRg
        
    def getNasc(self):
        """Retorna a instancia Data com a data de nascimento do aluno"""
        return self.__dataNasc
    def setNasc(self, novoNasc):
        """Edita a instancia Data com a data de nascimento do aluno"""
        self.__dataNasc = novoNasc
        
    def getResponsavel(self):
        """Retorna a instancia Responsavel do aluno"""
        return self.__responsavel
    def setResponsavel(self, novoResponsavel):
        """Edita a instancia Responsavel do aluno"""
        self.__responsavel = novoResponsavel
        
    def getEmail(self):
        """Retorna o email do aluno"""
        return self.__email
    def setEmail(self, novoEmail):
        """Edita o email do aluno"""
        self.__email = novoEmail
        
    def getTelefone(self):
        """Retorna o telefone do aluno"""
        return self.__telefone
    def setTelefone(self, novoTelefone):
        """Edita o telefone do aluno"""
        self.__telefone = novoTelefone
        
    def getEndereco(self):
        """Retorna a instancia Endereco do aluno"""
        return self.__endereco
    def setEndereco(self, novoEndereco):
        """Edita a instancia Endereco do aluno"""
        self.__endereco = novoEndereco

    def getLogin(self):
        """Retorna a instancia Login do aluno"""
        return self.__login
    def setLogin(self, novoLogin):
        """Edita a instacia Login do aluno"""
        self.__login = novoLogin

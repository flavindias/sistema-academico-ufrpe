class Responsavel:
    """Class de gerenciamento de responsaveis"""
    def __init__(self, nome, aluno, cpf, rg, sexo, email, telefone, endereco, login):
        """Cria um reponsavel por alunos"""
        self.__nome = nome
        self.__alunos = []
        self.__alunos.append(aluno)
        self.__cpf = cpf
        self.__rg = rg
        self.__sexo = sexo
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco
        self.__login = login

    def getNome(self):
        """Retorna o nome do responsavel"""
        return self.__nome
    def setNome(self, novoNome):
        """Edita o nome do responsavel"""
        self.__nome = novoNome

    def addAluno(self, aluno):
        """Adiciona um aluno a um responsavel"""
        if aluno in self.__alunos:
            return False
        else:
            self.__alunos.append(aluno)
            return True
    def getAlunos(self):
        """Retorna uma lista de instacias alunos sobre responsabilidade do responsavel"""
        return self.__aluno
    def excAluno(self, aluno):
        """Exclui um aluno da responsabilidade do responsavel"""
        if aluno in self.__alunos:
            del self.__alunos[self.__alunos.index(aluno)]
            return True
        else:
            return False
        
    def getCpf(self):
        """Retorna o CPF do responsavel"""
        return self.__cpf
    def setCpf(self, novoCpf):
        """Edita o CPF do responsavel"""
        self.__cpf = novoCpf

    def getRg(self):
        """Retorna o RG do responsavel"""
        return self.__rg
    def setRg(self, novoRg):
        """Edita o RG do responsavel"""
        self.__rg = novoRg
        
    def getEmail(self):
        """Retorna o email do responsavel"""
        return self.__email
    def setEmail(self, novoEmail):
        """Edita o email do responsavel"""
        self.__email = novoEmail
        
    def getTelefone(self):
        """Retorna o telefone do responsavel"""
        return self.__telefone
    def setTelefone(self, novoTelefone):
        """Edita o telefone do responsavel"""
        self.__telefone = novoTelefone
        
    def getEndereco(self):
        """Retorna a instancia Endereco do responsavel"""
        return self.__endereco
    def setEndereco(self, novoEndereco):
        """Edita a instancia Endereco do responsavel"""
        self.__endereco = novoEndereco

    def getLogin(self):
        """Retorna a instancia Login do responsavel"""
        return self.__login
    def setLogin(self, novoLogin):
        """Edita a instacia Login do responsavel"""
        self.__login = novoLogin

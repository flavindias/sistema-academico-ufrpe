#-------------------------------------------------------------------------------
# Name:        Aluno
# Purpose:     Classe de gerenciamento para instancias de alunos criadas
#
# Author:      Igor Mateus
#
# Created:     02/12/2011
# Copyright:   (c) AcademicSYS 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import DataBase

class Aluno:
    """Classe Aluno"""
    def setNome(self, novoNome):
        """Ajusta o nome"""
        self.__nome=novoNome
    def setCpf(self, novoCpf):
        """Ajusta o CPF"""
        self.__cpf=novoCpf
    def setData(self, novoData):
        """Ajusta a data"""
        self.__data=novoData
    def setUf(self, novoUf):
        """Ajusta o estado"""
        self.__uf=novoUf
    def setCidade(self, novoCidade):
        """Ajusta a cidade"""
        self.__cidade= novoCidade
    def setBairro(self, novoBairro):
        """Ajusta o bairro"""
        self.__bairro=novoBairro
    def setRua(self, novoRua):
        """Ajusta a rua"""
        self.__rua=novoRua
    def setNum(self, novoNum):
        """Ajusta o numero"""
        self.__num=novoNum
    def setComp(self, novoComp):
        """Ajusta o complemento"""
        self.__comp=novoComp
    def setTelefone(self, novoTelefone):
        """Ajusta o telefone fixo"""
        self.__telefone=novoTelefone
    def setCelular(self, novoCelular):
        """Ajusta o celular"""
        self.__celular=novoCelular
    def setSexo(self, novoSexo):
        """Ajusta o sexo"""
        self.__sexo=novoSexo
    def setSerie(self, novoSerie):
        """Ajusta a serie do aluno"""
        self.__serie=novoSerie
    def setTurno(self, novoTurno):
        """Ajusta o turno preferencial do aluno"""
        self.__turno=novoTurno
    def setCep(self, novoCep):
        """Ajusta o cep"""
        self.__cep = novoCep
    def getNome(self):
        """Retorna o nome"""
        return self.__nome
    def getCpf(self):
        """Retorna o CPF"""
        return self.__cpf
    def getData(self):
        """Retorna a data"""
        return self.__data
    def getUf(self):
        """Retorna o estado"""
        return self.__uf
    def getCidade(self):
        """Retorna a cidade"""
        return self.__cidade
    def getBairro(self):
        """Retorna o Bairro"""
        return self.__bairro
    def getRua(self):
        """Retorna a rua"""
        return self.__rua
    def getNum(self):
        """Retorna o numero"""
        return self.__num
    def getComp(self):
        """Retorna o complemento"""
        return self.__comp
    def getTelefone(self):
        """Retorna o telefone fixo"""
        return self.__telefone
    def getCelular(self):
        """Retorna o celular"""
        return self.__celular
    def getSexo(self):
        """Retorna o sexo"""
        return self.__sexo
    def getSerie(self):
        """Retorna a serie"""
        return self.__serie
    def getTurno(self):
        """Retorna o turno de preferencia do aluno"""
        return self.__turno
    def getCep(self):
        """Retorna o cep"""
        return self.__cep

    def __init__(self, cpf = None):
        """Inicia uma nova instancia"""
        if cpf == None:
            ##Nao carregando do BD
            self.setNome(None) #str len max 40
            self.setCpf(None) #str len 11
            self.setData(None) #str ex: ano-mes-dia
            self.setCep(None) #str len 8
            self.setUf(None) #str len 2
            self.setCidade(None) #str len max 20
            self.setBairro(None) #str len max 20
            self.setRua(None) #str len max 40
            self.setNum(None) #int positivo
            self.setComp(None) #str len max 100
            self.setTelefone(None) #str len 10 (sem caracteres especiais)
            self.setCelular(None) #str len 10 (sem caracteres especiais)
            self.setSexo(None) #int (1=Masculino / 2=Femenino)
            self.setSerie(None) #int len 1
            self.setTurno(None) #str len 1 (M=Manha / T=Tarde / N=Noite
        else:
            ##Carregando do BD
            self.carregar(cpf)

    def carregar(self, cpf):
        """Carrega um Aluno no BD a partir do CPF"""
        self.__result=DataBase.carregarAluno(cpf)
        self.setCpf(self.__result[0])
        self.setNome(self.__result[1])
        self.setData(str(self.__result[2]))
        self.setSexo(self.__result[3])
        self.setUf(self.__result[4])
        self.setCidade(self.__result[5])
        self.setBairro(self.__result[6])
        self.setRua(self.__result[7])
        self.setNum(self.__result[8])
        self.setComp(self.__result[9])
        self.setTelefone(self.__result[10])
        self.setCelular(self.__result[11])
        self.setSerie(self.__result[12])
        self.setTurno(self.__result[13])
        del self.__result

    def salvarEdit(self, cpf, nome=None, data=None, sexo=None, uf=None, cidade=None, bairro=None, rua=None, num=None, comp=None, telefone=None, celular=None, serie=None, turno=None):
        """Salva uma edicao no BD"""
        return DataBase.editarAluno([cpf, nome, data, sexo, uf, cidade, bairro, rua, num, comp, telefone, celular, serie, turno])

    def listaDb(self):
        """Retorna uma lista com todos os Professores do DB"""
        return DataBase.getListDbAluno()

    def add(self, cpf, nome, data, sexo, uf, cidade, bairro, rua, num, comp, serie, turno, telefone=None, celular=None):
        """Adiciona um Aluno no BD"""
        if cpf!= None and nome!=None and data!=None and sexo!=None and uf!=None and cidade!=None and bairro!=None and rua!=None and num!=None and comp!=None and serie!=None and turno!=None:
            return DataBase.addAluno(cpf, nome, data, sexo, uf, cidade, bairro, rua, num, comp, telefone, celular, serie, turno)
        else:
            return False

    def delete(self, cpf):
        """Deleta um aluno do BD"""
        return DataBase.deleteAluno(cpf)

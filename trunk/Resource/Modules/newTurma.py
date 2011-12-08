#-------------------------------------------------------------------------------
# Name:        Turma
# Purpose:     Classe de gerenciamento para instancias de turmas criadas
#
# Author:      Igor Mateus
#
# Created:     02/12/2011
# Copyright:   (c) AcademicSYS 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import DataBase

class Turma:
    """Classe Turma"""
    def setTurma(self, novoTurma):
        """Ajusta o nome da turma"""
        self.__turma=novoTurma
    def setTurno(self, novoTurno):
        """Ajusta o Turno"""
        self.__turno=novoTurno
    def setDisciplina1(self, novoDisciplina):
        """Ajusta a disciplina 1"""
        self.__disc1=novoDisciplina
    def setDisciplina2(self, novoDisciplina):
        """Ajusta a disciplina 2"""
        self.__disc2=novoDisciplina
    def setDisciplina3(self, novoDisciplina):
        """Ajusta a disciplina 3"""
        self.__disc3=novoDisciplina
    def setDisciplina4(self, novoDisciplina):
        """Ajusta a disciplina 4"""
        self.__disc4=novoDisciplina
    def setDisciplina5(self, novoDisciplina):
        """Ajusta a disciplina 5"""
        self.__disc5=novoDisciplina
    def setDisciplina6(self, novoDisciplina):
        """Ajusta a disciplina 6"""
        self.__disc6=novoDisciplina
    def setAlunos(self, novoAlunos):
        """"Ajusta uma tupla de alunos"""
        self.__alunos = novoAlunos
    def setHorario(self, novoHorario):
        """Ajusta o Horario"""
        self.__horario = novoHorario
    def getTurma(self):
        """Retorna o nome da turma"""
        return self.__turma
    def getTurno(self):
        """Retorna o turno"""
        return self.__turno
    def getDisciplina1(self):
        """Retorna o nome da disciplina1"""
        return self.__disc1
    def getDisciplina2(self):
        """Retorna o nome da disciplina2"""
        return self.__disc2
    def getDisciplina3(self):
        """Retorna o nome da disciplina3"""
        return self.__disc3
    def getDisciplina4(self):
        """Retorna o nome da disciplina4"""
        return self.__disc4
    def getDisciplina5(self):
        """Retorna o nome da disciplina5"""
        return self.__disc5
    def getDisciplina6(self):
        """Retorna o nome da disciplina6"""
        return self.__disc6
    def getAlunos(self):
        """Returna uma lista de alunos"""
        return self.__alunos
    def getHorario(self):
        """Retorna a lista de horario"""
        return self.__horario

    def __init__(self, turma=None):
        """Inicia uma nova instancia"""
        if turma == None:
            self.setTurma(None) #str len 3
            self.setTurno(None) #str len 1
            self.setDisciplina1(None) #str len max 20
            self.setDisciplina2(None) #str len max 20
            self.setDisciplina3(None) #str len max 20
            self.setDisciplina4(None) #str len max 20
            self.setDisciplina5(None) #str len max 20
            self.setDisciplina6(None) #str len max 20
            self.setAlunos(None) #[str] len 11
            self.setHorario(None) #[str] len max 20
        else:
            self.carregar(turma)

    def carregar(self, turma):
        """Carregar uma turma no BD a partir do nome"""
        self.__result=DataBase.carregarTurma(turma)
        if self.__result == None:
            return False
        else:
            self.setTurma(self.__result[0])
            self.setTurno(self.__result[1])
            self.setDisciplina1(self.__result[2])
            self.setDisciplina2(self.__result[3])
            self.setDisciplina3(self.__result[4])
            self.setDisciplina4(self.__result[5])
            self.setDisciplina5(self.__result[6])
            self.setDisciplina6(self.__result[7])
            self.carregarAluno(turma)
            self.setHorario(self.carregarHorario(turma))
            return True

    def salvarEdit(self, turma, turno=None, disciplina1=None, disciplina2=None, disciplina3=None, disciplina4=None, disciplina5=None, disciplina6=None):
        """Edita uma turma no BD"""
        return DataBase.editarTurma([turma, turno, disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6])

    def listaDb(self):
        """Retorna uma lista com todas as Turmas cadastradas no BD"""
        return DataBase.getListDbTurma()

    def add(self, turma, turno, disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6):
        """Adiciona uma Turma no BD"""
        return DataBase.addTurma(turma, turno, disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6)

    def delete(self, turma):
        """Deleta uma disciplina do BD"""
        for self.__i in self.getAlunos():
            self.deleteAluno(self.__i)
        self.deleteHorario(turma)
        return DataBase.deleteTurma(turma)

    def addAluno(self, turma, aluno):
        """Add aluno relacionado a turma direto no bd"""
        if DataBase.addTurma_Aluno(turma, aluno):
            self.carregarAluno(self.getTurma())
            return True
        else:
            return False

    def carregarAluno(self, turma):
        """Carrega todos os alunos relacionados a turma"""
        self.setAlunos(DataBase.carregarTurma_Alunos(turma))

    def deleteAluno(self, aluno):
        """Deleta aluno da tabela"""
        if DataBase.deleteTurma_Alunos(aluno):
            self.carregarAluno(self.getTurma())
            return True
        else:
            return False

    def addHorario(self, turma, disciplina1=None, disciplina2=None, disciplina3=None, disciplina4=None, disciplina5=None, disciplina6=None, disciplina7=None, disciplina8=None, disciplina9=None, disciplina10=None, disciplina11=None, disciplina12=None, disciplina13=None, disciplina14=None, disciplina15=None, disciplina16=None, disciplina17=None, disciplina18=None, disciplina19=None, disciplina20=None, disciplina21=None, disciplina22=None, disciplina23=None, disciplina24=None, disciplina25=None):
        """Add horario relacionado a turma direto no bd"""
        if DataBase.addTurma_Horario(turma, [disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6, disciplina7, disciplina8, disciplina9, disciplina10, disciplina11, disciplina13, disciplina14, disciplina15, disciplina16, disciplina17, disciplina18, disciplina19, disciplina20, disciplina21, disciplina22, disciplina23, disciplina24, disciplina25]):
            self.setHorario(self.carregarHorario(turma))
            return True
        else:
            return False

    def carregarHorario(self, turma):
        """Carrega Horarios relacionados a turma"""
        return DataBase.carregarTurma_Horario(turma)

    def deleteHorario(self, turma):
        """Deleta horario da tabela no BD"""
        if DataBase.deleteTurma_Horario(turma):
            self.setHorario(None)
            return True
        else:
            return False

    def listaDbHorario(self):
        """Retorna uma lista com todas as tabelas do sistema de horarios"""
        return DataBase.getListTurma_HorarioFromDb()

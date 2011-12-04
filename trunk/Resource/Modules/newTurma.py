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
import Turma_Aluno

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
            self.__result = Turma_Aluno.carregar(turma)
            self.setAlunos(self.__result)
            return True

    def salvarEdit(self, turma, turno=None, disciplina1=None, disciplina2=None, disciplina3=None, disciplina4=None, disciplina5=None, disciplina6=None):
        """Edita uma turma no BD"""
        return DataBase.editarTurma([turma, turno, disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6])

    def listaDb(self):
        """Retorna uma lista com todas as Turmas cadastradas no BD"""
        return DataBase.getListDbTurma()            

    def listaDbAluno(self, turma):
        """Retorna uma lista com todos os alunos de uma tuma do BD"""
        self.setAlunos(Database.carregarTurma_Alunos(turma))

    def add(self, turma, turno, disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6):
        """Adiciona uma Turma no BD"""
        return DataBase.addTurma(turma, turno, disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6)

    def delete(self, turma):
        """Deleta uma disciplina do BD"""
        Turma_Aluno.delete(turma)
        return DataBase.deleteTurma(turma)

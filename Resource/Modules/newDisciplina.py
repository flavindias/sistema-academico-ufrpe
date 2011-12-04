#-------------------------------------------------------------------------------
# Name:        Disciplina
# Purpose:     Classe de gerenciamento para instancias de disciplinas criadas
#
# Author:      Igor Mateus
#
# Created:     02/12/2011
# Copyright:   (c) AcademicSYS 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import DataBase

class Disciplina:
    """Classe disciplina"""
    def setDisciplina(self, novoDisciplina):
        """Ajusta a disciplina"""
        self.__disciplina=novoDisciplina
    def setProfessor(self, novoProfessor):
        """Ajusta o professor"""
        self.__professor=novoProfessor
    def getDisciplina(self):
        """Retorna o nome da Disciplina"""
        self.__disciplina
    def getProfessor(self):
        """Retorna um documento do professor"""
        return self.__professor

    def __init__(self, disciplina=None):
        """Inicia uma instacia Disciplina"""
        if disciplina == None:
            self.setDisciplina(None) #str len max 20
            self.setProfessor(None) #str len 11
        else:
            self.carregar(disciplina)

    def carregar(self, disciplina):
        """Carrega informacoes de uma disciplina do BD"""
        self.__result=DataBase.carregarDisciplina(disciplina)
        if self.__result == None:
            return False
        else:
            self.setDisciplina(self.__result[0])
            self.setProfessor(self.__result[1])
            del self.__result
            return True

    def salvarEdit(self, disciplina, professor):
        """Salva uma edicao de uma disciplina no BD"""
        return DataBase.editarDisciplina([disciplina, professor])

    def listaDb(self):
        """Returna uma lista com todos as disciplinas do BD"""
        return DataBase.getListDbDisciplina()

    def add(self, disciplina, professor):
        """Add uma disciplina no BD"""
        return DataBase.addDisciplina(disciplina, professor)

    def delete(self, disciplina):
        """Deleta uma disciplina do Banco de dados"""
        return DataBase.deleteDisciplina(disciplina)

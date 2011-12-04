#-------------------------------------------------------------------------------
# Name:        Turma_Aluno
# Purpose:     Classe de entre turmas e alunos
#
# Author:      Igor Mateus
#
# Created:     02/12/2011
# Copyright:   (c) AcademicSYS 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import DataBase

lista = []

def add(turma, aluno):
    """Add aluno relacionado a turma direto no bd"""
    return DataBase.addTurma_Aluno(turma, aluno)

def carregar(turma):
    """Carrega todos os alunos relacionados a turma"""
    return DataBase.carregarTurma_Alunos(turma)

def delete(aluno):
    """Deleta aluno da tabela"""
    return DataBase.deleteTurma_Alunos(aluno)

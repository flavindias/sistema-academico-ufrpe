#-------------------------------------------------------------------------------
# Name:        DataBase
# Purpose:     Faz conexoes com o BD para alimentar as classes
#
# Author:      Igor Mateus
#
# Created:     02/12/2011
# Copyright:   (c) AcademicSYS 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import base64
import MySQLdb

connection = MySQLdb.connect(host="db4free.net", db="academicsys", user="desenvolvedores", passwd="acesso")
cursor = connection.cursor()

def carregarAluno(cpf):
    """Carrega dados do aluno no BD"""
    try:
        cursor.execute("select * from Aluno where cpf = '%s';" %(cpf))
        result = cursor.fetchone()
        return result
    except:
        return [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

def editarAluno(lista):
    """Edita dados do aluno no BD"""
    try:
        if lista[0] == None:
            return False
        else:
            if lista[1] != None:
                cursor.execute("update Aluno set nome = '%s' where cpf = '%s';" %(lista[1], lista[0]))
            if lista[2] != None:
                cursor.execute("update Aluno set dat = '%s' where cpf = '%s';" %(lista[2], lista[0]))
            if lista[3] != None:
                cursor.execute("update Aluno set sexo = %s where cpf = '%s';" %(lista[3], lista[0]))
            if lista[4] != None:
                cursor.execute("update Aluno set cep = '%s' where cpf = '%s';" %(lista[4], lista[0]))
            if lista[5] != None:
                cursor.execute("update Aluno set uf = '%s' where cpf = '%s';" %(lista[5], lista[0]))
            if lista[6] != None:
                cursor.execute("update Aluno set cidade = '%s' where cpf = '%s';" %(lista[6], lista[0]))
            if lista[7] != None:
                cursor.execute("update Aluno set bairro = '%s' where cpf = '%s';" %(lista[7], lista[0]))
            if lista[8] != None:
                cursor.execute("update Aluno set rua = '%s' where cpf = '%s';" %(lista[8], lista[0]))
            if lista[9] != None:
                cursor.execute("update Aluno set num = %s where cpf = '%s';" %(lista[9], lista[0]))
            if lista[10] != None:
                cursor.execute("update Aluno set comp = '%s' where cpf = '%s';" %(lista[10], lista[0]))
            if lista[11] != None:
                cursor.execute("update Aluno set telefone = '%s' where cpf = '%s';" %(lista[11], lista[0]))
            if lista[12] != None:
                cursor.execute("update Aluno set celular = '%s' where cpf = '%s';" %(lista[12], lista[0]))
            if lista[13] != None:
                cursor.execute("update Aluno set serie = %s where cpf = '%s';" %(lista[13], lista[0]))
            if lista[14] != None:
                cursor.execute("update Aluno set turno = '%s' where cpf = '%s';" %(lista[14], lista[0]))
            return True
    except:
        return False

def getListDbAluno():
    """Busca todos os alunos no BD"""
    cursor.execute("select * from Aluno")
    return cursor.fetchone()

def addAluno(cpf, nome, data, sexo, uf, cidade, bairro, rua, num, comp, telefone, celular, serie, turno):
    """Adiciona um aluno no BD"""
    try:
        cursor.execute("insert into Aluno(cpf, nome, dat, sexo, uf, cidade, bairro, rua, num, comp, telefone, celular, serie, turno) values ('%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', %s, '%s', NULL, NULL, '%s', '%s');" %(cpf, nome, data, sexo, uf, cidade, bairro, rua, num, comp, serie, turno))
        if celular!=None:
            cursor.execute("update Aluno set celular = '%s' where cpf = '%s';" %(celular, cpf))
        if telefone!=None:
            cursor.execute("update Aluno set telefone = '%s' where cpf = '%s';" %(telefone, cpf))
        return True
    except:
        return False

def deleteAluno(cpf):
    """Deleta um aluno do BD"""
    try:
        cursor.execute("delete from Aluno where cpf = '%s';" %(cpf))
        return True
    except:
        return False


###PROFESSOR###
def carregarProfessor(cpf):
    """Carrega um Professor do BD"""
    try:
        cursor.execute("select * from Professor where cpf = '%s';" %(cpf))
        result = cursor.fetchone()
        return result
    except:
        return [None, None, None, None, None, None, None, None, None, None, None, None, None]
    
def editarProfessor(lista):
    """Edita um Professor no BD"""
    try:
        if lista[0] == None:
            return False
        else:
            if lista[1] != None:
                cursor.execute("update Professor set nome = '%s' where cpf = '%s';" %(lista[1], lista[0]))
            if lista[2] != None:
                cursor.execute("update Professor set dat = '%s' where cpf = '%s';" %(lista[2], lista[0]))
            if lista[3] != None:
                cursor.execute("update Professor set sexo = %s where cpf = '%s';" %(lista[3], lista[0]))
            if lista[4] != None:
                cursor.execute("update Professor set cep = '%s' where cpf = '%s';" %(lista[4], lista[0]))
            if lista[5] != None:
                cursor.execute("update Professor set uf = '%s' where cpf = '%s';" %(lista[5], lista[0]))
            if lista[6] != None:
                cursor.execute("update Professor set cidade = '%s' where cpf = '%s';" %(lista[6], lista[0]))
            if lista[7] != None:
                cursor.execute("update Professor set bairro = '%s' where cpf = '%s';" %(lista[7], lista[0]))
            if lista[8] != None:
                cursor.execute("update Professor set rua = '%s' where cpf = '%s';" %(lista[8], lista[0]))
            if lista[9] != None:
                cursor.execute("update Professor set num = %s where cpf = '%s';" %(lista[9], lista[0]))
            if lista[10] != None:
                cursor.execute("update Professor set comp = '%s' where cpf = '%s';" %(lista[10], lista[0]))
            if lista[11] != None:
                cursor.execute("update Professor set telefone = '%s' where cpf = '%s';" %(lista[11], lista[0]))
            if lista[12] != None:
                cursor.execute("update Professor set celular = '%s' where cpf = '%s';" %(lista[12], lista[0]))
            return True
    except:
        return False
    
def getListDbProfessor():
    """Busca todos os alunos no BD"""
    cursor.execute("select * from Professor")
    return cursor.fetchone()

def addProfessor(cpf, nome, data, sexo, cep, uf, cidade, bairro, rua, num, comp, telefone, celular):
    """Adiciona um professor no BD"""
    try:
        cursor.execute("insert into Professor(cpf, nome, dat, sexo, cep, uf, cidade, bairro, rua, num, comp, telefone, celular) values ('%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s', %s, '%s', NULL, NULL);" %(cpf, nome, data, sexo, cep, uf, cidade, bairro, rua, num, comp))
        if celular!=None:
            cursor.execute("update Professor set celular = '%s' where cpf = '%s';" %(celular, cpf))
        if telefone!=None:
            cursor.execute("update Professor set telefone = '%s' where cpf = '%s';" %(telefone, cpf))
        return True
    except:
        return False
    
def deleteProfessor(cpf):
    """Deleta um professor do BD"""
    try:
        cursor.execute("delete from Professor where cpf = '%s';" %(cpf))
        return True
    except:
        return False


###DISCIPLINA###    
def carregarDisciplina(disciplina):
    """Carrega uma disciplina do BD"""
    try:
        cursor.execute("select * from Disciplina where disciplina = '%s';" %(disciplina))
        return cursor.fetchone()
    except:
        return None
    
def editarDisciplina(lista):
    """Edita uma disciplina no BD"""
    try:
        if lista[0]!=None and lista[1]!=None:
            cursor.execute("update Disciplina set professor = '%s' where disciplina = '%s';" %(lista[1], lista[0]))
            return True
        else:
            return False
    except:
            return False

def getListDbDisciplina():
    """Busca todas as disciplinas do BD"""
    cursor.execute("select * from Disciplina;")
    return cursor.fetchall()

def addDisciplina(disciplina, professor):
    """Adiciona umad disciplina no BD"""
    try:
        cursor.execute("insert into Disciplina(disciplina, professor) values ('%s','%s');" %(disciplina, professor))
        return True
    except:
        return False
    
def deleteDisciplina(disciplina):
    """Deleta uma disciplina no BD"""
    try:
        cursor.execute("delete from Disciplina where disciplina = '%s';" %(disciplina))
        return True
    except:
        return False


###TURMA###
def carregarTurma(turma):
    """Carrega uma turma no BD"""
    try:
        cursor.execute("select * from Turma where turma = '%s';" %(turma))
        return cursor.fetchone()
    except:
        return [None, None, None, None, None, None, None, None]
    
def editarTurma(lista):
    """Edita um Turma no BD"""
    try:
        if lista[0] == None:
            return False
        else:
            if lista[1]!=None:
                cursor.execute("update Turma set turno = '%s' where turma = '%s';" %(lista[1], lista[0]))
            if lista[2]!=None:
                cursor.execute("update Turma set disciplina1 = '%s' where turma = '%s';" %(lista[2], lista[0]))
            if lista[3]!=None:
                cursor.execute("update Turma set disciplina2 = '%s' where turma = '%s';" %(lista[3], lista[0]))
            if lista[4]!=None:
                cursor.execute("update Turma set disciplina3 = '%s' where turma = '%s';" %(lista[4], lista[0]))
            if lista[5]!=None:
                cursor.execute("update Turma set disciplina4 = '%s' where turma = '%s';" %(lista[5], lista[0]))
            if lista[6]!=None:
                cursor.execute("update Turma set disciplina5 = '%s' where turma = '%s';" %(lista[6], lista[0]))
            if lista[7]!=None:
                cursor.execute("update Turma set disciplina6 = '%s' where turma = '%s';" %(lista[7], lista[0]))
            return True
    except:
        return False
    
def getListDbTurma():
    """Busca todas as turmas no BD"""
    cursor.execute("select * from Turma;")
    return cursor.fetchall()

def getListDbTurma_Aluno(turma):
    """Busca todos os alunos da turma no BD"""
    
def addTurma(turma, turno, disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6):
    """Adiciona uma turma no BD"""
    try:
        if turma!=None and turno!=None and disciplina1!=None and disciplina2!=None and disciplina3!=None and disciplina4!=None and disciplina5!=None and disciplina6!=None:
            cursor.execute("insert into Turma(turma, turno, disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" %(turma, turno, disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6))
            return True
        else:
            return False
    except:
        return False

def deleteTurma(turma):
    """Deleta uma turma do BD"""
    try:
        if turma != None:
            cursor.execute("delete from Turma where turma = '%s';" %(turma))
            return True
        else:
            return False
    except:
        return False


###LOGIN###    
def carregarLogin(login):
    """Carrega um Login no BD"""
    try:
        cursor.execute("select * from Login where login = '%s';" %(login))
        result = cursor.fetchone()
        lista = []
        lista.append(result[0])
        lista.append(base64.b64decode(result[1]))
        lista.append(result[1])
        return lista
    except:
        return [None, None, None]
    
def editarLogin(login, senha, tipo):
    """Edita um login no BD"""
    try:
        if login == None:
            return False
        else:
            if senha!=None:
                cursor.execute("update Login set senha = '%s' where login = '%s';" %(base64.b64encode(senha), login))
            if tipo!=None:
                cursor.execute("update Turma set tipo = '%s' where login = '%s';" %(tipo, login))
            return True
    except:
        return False
    
def getListDbLogin():
    """Busca todos os logins do BD"""
    try:
        cursor.execute("select * from Login;")
        return cursor.fetchall()
    except:
        return None
    
def addLogin(login, senha, tipo):
    """Adiciona um login no BD"""
    try:
        if login!=None and senha!=None and tipo!=None and len(tipo)==3:
            cursor.execute("insert into Login(login, senha, tipo) values ('%s', '%s', '%s');" %(login, base64.b64encode(senha), tipo))
            return True
        else:
            return False
    except:
        return False
    
def deleteLogin(login):
    """Deleta um login do BD"""
    try:
        if login!=None:
            cursor.execute("delete from Login where login = '%s';" %(login))
            return True
        else:
            return False
    except:
        return False


###TURMA_ALUNO###    
def addTurma_Aluno(turma, aluno):
    """Atrela um aluno a uma turma"""
    try:
        if turma != None and aluno != None:
            cursor.execute("insert into Turma_Aluno(aluno, turma) values ('%s', '%s');" %(aluno, turma))
            return True
        else:
            return False
    except:
        return False
    
def carregarTurma_Alunos(turma):
    """Carrega alunos da turma"""
    try:
        if turma != None:
            cursor.execute("select aluno from Turma_Aluno where turma = '%s';" %(turma))
            return cursor.fetchall()
        else:
            return None
    except:
        return None
    
def deleteTurma_Alunos(aluno):
    """Deleta todos as relacoes de todos os alunos com a turma a ser deletada"""
    try:
        if aluno!=None:
            cursor.execute("delete from Turma_Aluno where aluno = '%s';" %(aluno))
            return True
        else:
            return False
    except:
        return False

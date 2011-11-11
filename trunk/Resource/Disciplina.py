import pickle

class Disciplina:

    def __init__(self, nome):
        self.nome = nome
        self.listaTurma = []
        self.listaProf = []

    def getNome(self):
        return self.nome

    def setNome(self, novoNome):
        self.nome = novoNome

    def addTurma(self, turma):
        if turma in self.listaTurma:
            return False
        else:
            self.listaTurma.append(turma)
            return True

    def excTurma(self, turma):
        if turma in self.listaTurma:
            del self.listaTurma[self.listaTurma.index(turma)]
            return True
        else:
            return False

    def getTurmas(self):
        return self.listaTurma

    def addProf(self, prof):
        if prof in self.listaProf:
            return False
        else:
            self.listaProf.append(prof)
            return True
        
    def excProf(self, prof):
        if prof in self.listaProf:
            del self.listaProf[self.listaProf.index(prof)]
            return True
        else:
            return False

    def getProfs(self):
        return self.listaProf


class Grade:
    """Gerencia as disciplinas"""
    def __init__(self):
        try:
            self.grade = carregar()
        except:
            self.grade = []
        
            
    def add(self, disciplina):
        try:
            self.grade = carregar()
        except:
            self.grade = []
            
        if disciplina in self.grade:
            return False
        else:
            self.grade.append(disciplina)
            salvar(self.grade)
            return True

    def exc(self, disciplina):
        try:
            self.grade = carregar()
        except:
            self.grade = []
            
        if disciplina in self.grade:
            del self.grade[self.grade.index(disciplina)]
            salvar(self.grade)
            return True
        else:
            return False
        
    def getGrade(self):
        try:
            self.grade = carregar()
        except:
            self.grade = []
        return self.grade

def salvar(grade):
    arquivo = open('disc.txt', 'wb')
    pickle.dump(grade, arquivo)
    arquivo.close()

def carregar():
    arquivo = open('disc.txt', 'rb')
    grade = pickle.load(arquivo)
    arquivo.close()
    return grade

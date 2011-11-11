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
        if nome in self.listaTurma:
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
        return self.listProf


class Grade:
    """Gerencia as disciplinas"""
    def __init__(self):
        self.grade = []

    def __carregar(self):
        try:
            arquivo = open('disc.txt', 'rb')
            self.grade = pickle.load(arquivo)
            arquivo.close()
        except:
            pass
            
    def add(self, disciplina):
        self.__carregar()
        if disciplina in self.grade:
            return False
        else:
            self.grade.append(disciplina)
            self.__salvar()
            return True

    def exc(self, disciplina):
        self.__carregar()
        if disciplina in self.grade:
            del self.grade[self.grade.index(disciplina)]
            self.__salvar()
            return True
        else:
            return False
        
    def getGrade(self):
        self.__carregar()
        return self.grade

    def __salvar(self):
        try:
            arquivo = open('dados.txt', 'wb')
            pickle.dump(self.grade, arquivo)
            arquivo.close()
        except:
            pass

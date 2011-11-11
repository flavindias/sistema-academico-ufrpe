class Data:
    """Classe Data"""

    def __init__(self, dia, mes, ano, hora, minut, seg):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__hora = hora
        self.__minut = minut
        self.__seg = seg

    def getDia(self):
        """Retorna o dia da data"""
        return self.__dia
    def setDia(self, novoDia):
        """Edita o dia da data"""
        self.__dia = novoDia

    def getMes(self):
        """Retorna o mes da data"""
        return self.__mes
    def setMes(self, novoMes):
        """Edita o mes da data"""
        self.__mes = novoMes

    def getAno(self):
        """Retorna o ano da data"""
        return self.__ano
    def setAno(self, novoAno):
        """Edita o ano da data"""
        self.__ano = novoAno

    def getHora(self):
        """Retorna a hora"""
        return self.__hora
    def setHora(self, novaHora):
        """Edita a hora"""
        self.__hora = novaHora

    def getMinut(self):
        """Retorna o minuto"""
        return self.__minut
    def setMinut(self, novoMinut):
        """Edita o minuto"""
        self.__minut = novoMinut

    def getSeg(self):
        """Retorna os segundos"""
        return self.__seg
    def setSeg(self, novoSeg):
        """Edita os segundos"""
        self.__seg = novoSeg

    def getDataComp(self):
        """Retorna a data completa"""
        return self.__dia + "-" + self.__mes + "-" + self.__ano

    def getHoraComp
        """Retorna a hora completa"""
        return self.__hora + ":" + self.__minut + ":" + self.__seg

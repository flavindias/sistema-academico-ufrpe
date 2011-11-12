class db:
    """Classe gerente de banco de dados"""
    def __init__(self):
        self.connection = MySQLdb.connect(host="www.freesql.org", user="ufrpeacademic", passwd="acesso", db="academicsis")

        

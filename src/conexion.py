import pymysql

class Conexion:    
    def __init__(self):
        self._ServidorDB = "localhost"
        self._UsuarioDB = "root"
        self._PasswordDB = "root"
        self._SchemaDB = "bdpy"
    def conecta(self):
        db = pymysql.connect(self._ServidorDB,self._UsuarioDB, self._PasswordDB,  
        self._SchemaDB,port=3306)
        return db

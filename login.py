class Login:
    def __init__(self, miDB):
        self.mysql = miDB
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def exito(self, id, contra):
        sql=f"SELECT nombre FROM usuarios WHERE id='{id}' AND contrasena='{contra}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado

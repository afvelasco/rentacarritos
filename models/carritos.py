'''
Esta clase tendrá como responsabilidad el manejo de la
persistencia asociada a la tabla de carritos
'''
from conexion import *
from datetime import datetime
import os

class Carro:
    def __init__(self, miDB,prog):
        self.mysql = miDB
        self.programa = prog
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def consultar(self):
        sql = "SELECT * FROM carritos WHERE borrado=0"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def buscar(self, pla):
        sql = f"SELECT placa FROM carritos WHERE placa = '{pla}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        if(len(resultado)==0):
             return False
        else:
             return True

    def agregar(self, carrito):
        now = datetime.now()
        tiempo = now.strftime("%Y%m%d%H%M%S")
        if carrito[6].filename != "":
            nombre,extension = os.path.splitext(carrito[6].filename)
            nuevoNombre = "F" + tiempo + extension
            carrito[6].save("uploads/"+nuevoNombre)
        sql = f"INSERT INTO carritos (placa,tipo,valhora,valsemana,color,modelo,kilometraje,disponibilidad,foto) VALUES ('{carrito[0]}',{carrito[1]},{carrito[2]},{carrito[3]},'{carrito[4]}',{carrito[5]},0,1,'{nuevoNombre}')"
        self.cursor.execute(sql)
        self.conexion.commit()

    def buscarPlaca(self, pla):
        sql=f"SELECT * FROM carritos WHERE placa='{pla}'"
        self.cursor.execute(sql)
        car = self.cursor.fetchall()
        self.conexion.commit()
        return car[0]
    
    def modificar(self,carrito):
        sql=f"UPDATE carritos SET tipo={carrito[1]},valHora={carrito[2]},valSemana={carrito[3]},modelo={carrito[5]},color='{carrito[4]}' WHERE placa='{carrito[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()
        if carrito[6].filename != "":
            # Subir la foto nueva
            now = datetime.now()
            tiempo = now.strftime("%Y%m%d%H%M%S")
            nombre,extension = os.path.splitext(carrito[6].filename)
            nuevoNombre = "F" + tiempo + extension
            carrito[6].save("uploads/"+nuevoNombre)
            # Consultar y borrar la foto vieja
            sql = f"SELECT foto FROM carritos WHERE placa='{carrito[0]}'"
            self.cursor.execute(sql)
            fotoVieja = self.cursor.fetchall()
            self.conexion.commit()
            os.remove(os.path.join(self.programa.config['CARPETAU'],fotoVieja[0][0]))
            # Actualizo nombre de la nueva foto en la db
            sql = f"UPDATE carritos SET foto='{nuevoNombre}' WHERE placa='{carrito[0]}'"
            self.cursor.execute(sql)
            self.conexion.commit()
    
    def borrar(self,pla):
        sql=f"UPDATE carritos SET BORRADO=1 WHERE placa='{pla}'"
        self.cursor.execute(sql)
        self.conexion.commit()
        
losCarritos = Carro(mysql,programa)


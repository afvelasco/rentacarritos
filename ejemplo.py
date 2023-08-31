from flask import Flask
from flaskext.mysql import MySQL
import hashlib

programa = Flask(__name__)
mysql = MySQL()
programa.config['MYSQL_DATABASE_HOST']='localhost'
programa.config['MYSQL_DATABASE_PORT']=3306
programa.config['MYSQL_DATABASE_USER']='root'
programa.config['MYSQL_DATABASE_PASSWORD']=''
programa.config['MYSQL_DATABASE_DB']='rentacarritos'
mysql.init_app(programa)

id = input("Digite ID: ")
nombre = input("Digite Nombre: ")
clave = input("Digite una contraseña: ")
cifrada = hashlib.sha512(clave.encode("utf-8")).hexdigest()
sql = f"INSERT INTO usuarios (id, nombre, contrasena) VALUES ('{id}','{nombre}','{cifrada}')"
conn = mysql.connect()
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()

from datetime import timedelta  # Lo usaremos para controlar el tiempo de la sesion
from random import randint  
from flask import Flask # session es para el manejo de sesiones
from flaskext.mysql import MySQL
import os

programa = Flask(__name__)
programa.secret_key=str(randint(10000,99999))  # Necesario para controlar la creación única de sesiones
programa.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes = 3)   # define la duración de la sesion
mysql = MySQL()
programa.config['MYSQL_DATABASE_HOST']='localhost'
programa.config['MYSQL_DATABASE_PORT']=3306
programa.config['MYSQL_DATABASE_USER']='root'
programa.config['MYSQL_DATABASE_PASSWORD']=''
programa.config['MYSQL_DATABASE_DB']='rentacarritos'
mysql.init_app(programa)
CARPETAU = os.path.join('uploads')
programa.config['CARPETAU']=CARPETAU
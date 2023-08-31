from datetime import timedelta  # Lo usaremos para controlar el tiempo de la sesion
from random import randint  
from flask import Flask, render_template, request, redirect, session # session es para el manejo de sesiones
from flask import send_from_directory
from flaskext.mysql import MySQL
import hashlib
import os
from datetime import datetime
from carritos import Carro
from login import Login

programa = Flask(__name__)
programa.secret_key=str(randint(10000,99999))  # Necesario para controlar la creación única de sesiones
programa.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes = 30)   # define la duración de la sesion
mysql = MySQL()
programa.config['MYSQL_DATABASE_HOST']='localhost'
programa.config['MYSQL_DATABASE_PORT']=3306
programa.config['MYSQL_DATABASE_USER']='root'
programa.config['MYSQL_DATABASE_PASSWORD']=''
programa.config['MYSQL_DATABASE_DB']='rentacarritos'
mysql.init_app(programa)
losCarritos = Carro(mysql,programa)
loguear = Login(mysql)
CARPETAU = os.path.join('uploads')
programa.config['CARPETAU']=CARPETAU

@programa.route('/uploads/<nombre>')
def uploads(nombre):
    return send_from_directory(programa.config['CARPETAU'],nombre)

@programa.route('/')
def index():
    session["logueado"] = False
    return render_template('/index.html')

@programa.route("/login", methods=['POST'])
def login():
    id = request.form['txtId']
    contra = request.form['txtContra']
    cifrada = hashlib.sha512(contra.encode("utf-8")).hexdigest()
    resultado = loguear.exito(id, cifrada)
    if(len(resultado)>0):
        session["logueado"] = True
        session["usuario_id"] = id
        session["usuario_nombre"] = resultado[0][0]
        return render_template("/principal.html")
    return render_template('/index.html')


@programa.route("/carritos")
def carritos():
    if session.get("logueado"):
        resultado = losCarritos.consultar()
        return render_template('/carritos.html', car=resultado, nom=session.get("usuario_nombre"))
    else:
        return render_template('/index.html')

@programa.route("/agregacarrito")
def agregacarrito():
    if session.get("logueado"):
        carro = ['',0,0,0,'',0,'']
        return render_template('agregacar.html', carro=carro)
    else:
        return render_template('/index.html')

@programa.route("/guardacar", methods=['POST'])
def guardacar():
    if session.get("logueado"):
        pla = request.form['txtPlaca']
        tip = request.form['txtTipo']
        vHo = request.form['txtValHora']
        vSe = request.form['txtValSem']
        col = request.form['txtColor']
        mod = request.form['txtModelo']
        foto = request.files['txtFoto']
        if not losCarritos.buscar(pla):
            losCarritos.agregar([pla,tip,vHo,vSe,col,mod,foto])
            return redirect('/carritos')
        else:
            mensaje="Placa ya existente"
            carro =["",tip,vHo,vSe,col,mod,foto]
            return render_template('agregacar.html', mensaje=mensaje, carro=carro)
    else:
        return render_template('/index.html')

@programa.route("/editarcar/<pla>")
def editarcar(pla):
    if session.get("logueado"):
        car = losCarritos.buscarPlaca(pla)
        return render_template('actualizacar.html',car=car)
    else:
        return render_template('/index.html')

@programa.route("/modificacar", methods=['POST'])
def modificacar():
    if session.get("logueado"):
        pla = request.form['txtPlaca']
        tip = request.form['txtTipo']
        vHo = request.form['txtValHora']
        vSe = request.form['txtValSem']
        col = request.form['txtColor']
        mod = request.form['txtModelo']
        foto = request.files['txtFoto']
        losCarritos.modificar([pla,tip,vHo,vSe,col,mod,foto])
        return redirect('/carritos')
    else:
        return render_template('/index.html')

@programa.route('/borracar/<pla>')
def borracar(pla):
    if session.get("logueado"):
        losCarritos.borrar(pla)
        return redirect('/carritos')
    else:
        return render_template('/index.html')

@programa.route('/clientes')
def clientes():
    return render_template('/clientes.html')

@programa.route('/rentas')
def rentas():
    if session.get("logueado"):
        sentencia = "SELECT idrenta,rentas.placa,rentas.licencia,clientes.nombre,fecha1,kilometraje1,observaciones FROM rentas INNER JOIN clientes ON rentas.licencia=clientes.licencia WHERE rentas.borrado=0"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sentencia)
        resultado = cursor.fetchall()
        conn.commit()
        print(resultado)
        return render_template('/rentas.html', ren=resultado, nom=session.get("usuario_nombre"))
    else:
        return render_template('/index.html')

@programa.route('/agregarenta')
def agregarenta():
    if session.get("logueado"):
        sentencia = "SELECT placa FROM carritos WHERE borrado=0 AND disponibilidad=1"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sentencia)
        carros = cursor.fetchall()
        conn.commit()
        sentencia = "SELECT licencia,nombre FROM clientes WHERE borrado=0"
        cursor.execute(sentencia)
        clientes = cursor.fetchall()
        conn.commit()
        return render_template('agregarenta.html', car = carros, cli = clientes)
    else:
        return render_template('/index.html')

@programa.route('/guardarenta', methods=['POST'])
def guardarenta():
    pla = request.form['txtPlaca']
    cli = request.form['txtLicencia']
    fec = request.form['txtFecha']
    sql = f"UPDATE carritos SET disponibilidad=0 WHERE placa='{pla}'"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    sql = f"SELECT kilometraje FROM carritos WHERE placa='{pla}'"
    cursor.execute(sql)
    kil = cursor.fetchone()
    conn.commit()
    sql = f"INSERT INTO rentas (placa,licencia,fecha1,kilometraje1) VALUES ('{pla}','{cli}','{fec}',{kil[0]})"
    cursor.execute(sql)
    conn.commit()
    return render_template("/rentas.html")
if __name__ == '__main__':
    programa.run(host='0.0.0.0', debug=True, port="5080")

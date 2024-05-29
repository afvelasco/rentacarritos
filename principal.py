from flask import render_template, request, session # session es para el manejo de sesiones
from flask import send_from_directory
from routes.carritos import carritos
from routes.login import login
from conexion import *

@programa.route('/uploads/<nombre>')
def uploads(nombre):
    return send_from_directory(programa.config['CARPETAU'],nombre)

@programa.route('/')
def index():
    session["logueado"] = False
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

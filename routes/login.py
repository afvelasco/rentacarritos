import hashlib
from flask import render_template, request, session
from conexion import *
from models.login import loguear

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

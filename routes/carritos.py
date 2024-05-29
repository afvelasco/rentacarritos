from flask import redirect, render_template, request, session
from conexion import *
from models.carritos import losCarritos

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

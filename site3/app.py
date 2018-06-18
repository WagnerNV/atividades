#coding: utf-8
from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/")
def pagina_index():
    return render_template("index.html")
	
@app.route("/metodo1/")
def dados2():
    nome = request.args.get("nome")
    email = request.args.get("email")
    telefone = request.args.get("telefone")
    return render_template("dados.html", **locals() )

@app.route("/metodo2/", methods=["POST"])
def dados():
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    return render_template("dados.html", **locals() )
	
@app.route("/dados/<nome>/<email>/<telefone>/")
def pagina_dados (nome, email, telefone):
    return render_template("index.html", **locals())
	
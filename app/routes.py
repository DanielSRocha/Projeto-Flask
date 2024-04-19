from app.models import usuario
from app.models import produto
from app.models import compra
from app import db
from app.forms import LoginForm
from datetime import timedelta
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

def init_app(app):
        
    #@app.route("/")
    #def principal():        
        #return render_template("seu_job/index.html")
    
    @app.route("/")
    def inicio():        
        return render_template("/inicio.html", usuarios=db.session.execute(db.select(usuario).order_by(usuario.id)).scalars())
    
    @app.route("/produtos")
    def produtos():        
        return render_template("produtos.html", produtos=db.session.execute(db.select(produto).order_by(produto.id)).scalars())
    
    @app.route("/compras")
    def compras():        
        return render_template("compras.html", compras=db.session.execute(db.select(compra).order_by(compra.id)).scalars())
    
    @app.route("/excluir/<int:id>")
    def excluir_user(id):
        delete=usuario.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("inicio"))
    
    @app.route("/excluir_prod/<int:id>")
    def excluir_prod(id):
        delete=produto.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("produtos"))
    
    @app.route("/excluir_compr/<int:id>")
    def excluir_compr(id):
        delete=compra.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("compras"))
    
    @app.route("/cad_user", methods=["GET", "POST"])
    def cad_user():        
        if request.method == "POST":
            user = usuario()
            user.email = request.form["email"]
            user.nome = request.form["nome"]        
            user.senha = generate_password_hash(request.form["senha"])
            db.session.add(user)
            db.session.commit()
                            
            flash("Usuario criado com sucesso!")       
            return redirect(url_for("cad_user"))
        return render_template("cad_user.html")
    
    @app.route("/cad_prod", methods=["GET", "POST"])
    def cad_prod():        
        if request.method == "POST":
            prod = produto()
            prod.nome = request.form["nome"]
            prod.descricao = request.form["descricao"]        
            prod.tamanho = request.form["tamanho"] 
            prod.quantidade = request.form["quantidade"] 
            prod.valor = request.form["valor"] 
            db.session.add(prod)
            db.session.commit()
                            
            flash("produto criado com sucesso!")       
            return redirect(url_for("cad_prod"))
        return render_template("cad_prod.html")
    
    @app.route("/cad_compr", methods=["GET", "POST"])
    def cad_compr():        
        if request.method == "POST":
            compr = compra()
            compr.cliente = request.form["cliente"]
            compr.produto = request.form["produto"]        
            compr.quantidade = request.form["quantidade"]
            compr.valor = request.form["valor"]
            db.session.add(compr)
            db.session.commit()
                            
            flash("compra criado com sucesso!")       
            return redirect(url_for("cad_compr"))
        return render_template("cad_compr.html")
    
    @app.route("/atualiza_user/<int:id>", methods=["GET", "POST"])
    def atualiza_user(id):
        user01=usuario.query.filter_by(id=id).first()
        if request.method == "POST":
            nome_usuario = request.form["nome"]
            email_usuario = request.form["email"]        
            senha = generate_password_hash(request.form["senha"])
            
            flash("Usuario alterado com sucesso!")     

            user01.query.filter_by(id=id).update({"email":email_usuario, "nome":nome_usuario, "senha":senha })
            db.session.commit()
            return redirect(url_for("inicio"))
        return render_template("atualiza_user.html", users=user01) 
    
    @app.route("/atualiza_prod/<int:id>", methods=["GET", "POST"])
    def atualiza_prod(id):
        prod01=produto.query.filter_by(id=id).first()
        if request.method == "POST":
            nome_produto = request.form["nome"]
            descricao_produto = request.form["descricao"]
            tamahno_produto = request.form["tamanho"]
            quantidade_produto = request.form["quantidade"]
            valor_produto = request.form["valor"]
            
            flash("produto alterado com sucesso!")     

            prod01.query.filter_by(id=id).update({"nome":nome_produto, "descricao":descricao_produto, "tamanho":tamahno_produto, "quantidade":quantidade_produto, "valor": valor_produto})
            db.session.commit()
            return redirect(url_for("produtos"))
        return render_template("atualiza_prod.html", prods=prod01) 
    
    @app.route("/atualiza_compr/<int:id>", methods=["GET", "POST"])
    def atualiza_compr(id):
        compr01=compra.query.filter_by(id=id).first()
        if request.method == "POST":
            cliente_compra = request.form["cliente"]
            produto_compra = request.form["produto"]
            quantidade_compra = request.form["quantidade"]
            valor_compra = request.form["valor"]
            
            flash("produto alterado com sucesso!")     

            compr01.query.filter_by(id=id).update({"cliente":cliente_compra, "produto":produto_compra, "quantidade":quantidade_compra, "valor": valor_compra})
            db.session.commit()
            return redirect(url_for("compras"))
        return render_template("atualiza_compr.html", compr=compr01) 
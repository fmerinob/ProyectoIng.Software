from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///itamizador.db'
db = SQLAlchemy(app)

class Evento(db.Model):
    idEvent = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(200), nullable = False)
    horaIni = db.Column(db.DateTime, default=datetime.utcnow)
    horaFin = db.Column(db.DateTime, default=datetime.utcnow)
    desc = db.Column(db.String(300), nullable = True)
    userID = db.Column(db.Integer, db.ForeignKey('usuario.idUser'), nullable = False)

    def __repr__(self):
        return '<Event %r>' % self.idEvent

class Usuario(db.Model):
    idUser = db.Column(db.Integer,primary_key=True)
    nombreU = db.Column(db.String(50),nullable = False)
    nomU = db.Column(db.String(50),nullable = False)
    correo = db.Column(db.String(75),nullable = False)
    pwd = db.Column(db.String(75),nullable = False)

    def __repr__(self):
        return '<User %r>' % self.idUser

@app.route('/', methods = ['POST'])
def index():
    nombre = request.form.get('NombreReg')
    username = request.form.get('userReg')
    mail = request.form.get('mailReg')
    password = request.form.get('pwdReg')
    
    new_user = Usuario(nombreU=nombre,nomU=username,correo=mail,pwd=password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return redirect('/') 
    except:
       return 'No se pudo registrar al usuario'
        
    usuarios = Usuario.query.order_by(Usuario.nomU).all()
    return render_template('index.html', users=usuarios)

@app.route('/home', methods = ['POST'])
def creaEvento():
    evento = request.form['altaEv']
    new_event = Usuario(evento)

    try:
        db.session.add(new_event)
        db.session.commit()
        return redirect('/') 
    except:
       return 'No se pudo registrar al usuario'
        
    usuarios = Usuario.query.order_by(Usuario.nomU).all()
    return render_template('index.html', users=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
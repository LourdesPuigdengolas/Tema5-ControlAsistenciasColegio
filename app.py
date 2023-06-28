from flask import Flask, render_template
from run import app, db

#from preceptor import db
from preceptor import Preceptor
from curso import Curso
from estudiante import Estudiante
from asistencia import Asistencia

#db = SQLAlchemy(app)

@app.route('/')
def index():
    preceptor = Preceptor('Juan', 'Perez', 'juan@gmail.com', '1234')
    db.session.add(preceptor)
    db.session.commit()
    return render_template('index.html') # esto me lleva a la pagina index.html y asi puedo hacer con las otras
    #lugo de validar el usuario me tendría que dirigir al html de preceptor

#caso de ejemplo para login luego de presionar el boton ingresar
@app.route('/login')
def login():
    isLoged = gestor.verifyUser()
    if isLoged:
        return render_template('preceptor.html')
    else:
        return render_template('index.html')#mostrar el error en la pagina de login

if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)

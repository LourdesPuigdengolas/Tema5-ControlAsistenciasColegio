from flask import render_template, session, redirect, request
from run import app, db
from gestorLogin import GestorLogin

from preceptor import Preceptor
from curso import Curso
from estudiante import Estudiante
from asistencia import Asistencia
from padre import Padre

@app.route('/')
def index():
    return render_template('index.html') # esto me lleva a la pagina index.html y asi puedo hacer con las otras
    #lugo de validar el usuario me tendría que dirigir al html de preceptor

#caso de ejemplo para login luego de presionar el boton ingresar
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        #db.session.query(Preceptor).filter(Preceptor.id==8).delete()
        #db.session.commit()
        #preceptor = Preceptor('Juan', 'Perez', 'fa_-_-_96@hotmail.com', '32164702f8ffd2b418d780ff02371e4c')
        #db.session.add(preceptor)
        #db.session.commit()

        gestorLogin = GestorLogin(request.form['email'], request.form['password'])
        userId = gestorLogin.verifyUserAndGetId()
        if userId:
            session['id'] = userId
            session['email'] = request.form['email']
            return redirect('/preceptor')
    
    return render_template('index.html')#mostrar el error en la pagina de login

@app.route('/preceptor')
def preceptor():
    if 'email' in session:
        return render_template('preceptor.html')
    else:
        return redirect('/')



@app.route('/logout')
def logout():
    session.pop('email', None) #pop me elimina la clave email del diccionario session
    session.pop('password', None)
    return redirect('/')



if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)

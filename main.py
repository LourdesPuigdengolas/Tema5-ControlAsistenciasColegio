from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key='CLAVE SECRETA'

@app.route('/')
def index():
    return render_template('index.html') # esto me lleva a la pagina index.html y asi puedo hacer con las otras
    #lugo de validar el usuario me tendría que dirigir al html de preceptor

#caso de ejemplo para login luego de presionar el boton ingresar
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        return redirect('/preceptor')
    else:
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
    app.run()

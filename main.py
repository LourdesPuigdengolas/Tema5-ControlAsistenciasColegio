from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
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
    app.run()

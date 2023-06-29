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


'''@app.route('/listarAsistencias', methods=['GET','POST'])
def listarAsistencias():
    if request.method == 'GET':
        return redirect('/preceptor')
    else:
        asistencias = Asistencia.query.all()
        return render_template('listarAsistencias.html', asistencias=asistencias)'''

@app.route('/listarCursoPorPreceptor', methods=['GET','POST'])
def listarCursoPorPreceptor():
    if request.method == 'GET':
        #cursos = Curso.query.all()
        return render_template('listaCursos.html')

    
@app.route('/listarEstudiantesPorCurso', methods=['GET','POST'])
def listarEstudiantesPorCurso():
    if request.method == 'GET':
        estudiantes = Estudiante.query.all()
        return render_template('listarEstudiantesPorCurso.html', estudiantes=estudiantes)

@app.route('/agregarAsistencia', methods=['GET','POST'])
def agregarAsistencia():
    if request.method == 'GET':
        idEstudiante = request.form['idEstudiante']
        fecha = request.form['fecha']
        estado = request.form['estado']
        asistencia = Asistencia(idEstudiante, fecha, estado)
        db.session.add(asistencia)
        db.session.commit()
        return redirect('/preceptor')
    else:
        return render_template('agregarAsistencia.html')


if __name__ == '__main__':
    app.run()

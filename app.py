# Importamos las clases y funciones necesarias de los módulos flask y flask_sqlalchemy.
from flask  import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # Creamos una nueva instancia de la clase Flask, que representa nuestra aplicación web.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db' # Configuramos la base de datos que vamos a utilizar
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desactiva las notificaciones de cambios en la base de datos
db = SQLAlchemy(app) # Creamos una nueva instancia de la clase Flask, que representa nuestra aplicación web.

class Task(db.Model): # Creamos una nueva clase llamada Task que hereda de la clase db.Model.
    id = db.Column(db.Integer, primary_key=True) # Creamos un campo id de tipo Integer que es la clave primaria de la tabla.
    content = db.Column(db.String(200), nullable=False) # Creamos un campo content de tipo String que no puede ser nulo.

    def __repr__(self):
        return f'Task({self.content})' # Devuelve una representación de cadena de la tarea.

@app.route('/') # Definimos una nueva vista que maneja las solicitudes a la raíz de nuestro sitio web.
def index():
    tasks = Task.query.all() # Obtenemos todas las tareas de la base de datos.
    return render_template('index.html', tasks=tasks) # Renderizamos la plantilla index.html y pasamos las tareas como contexto.

@app.route('/add', methods=['POST'])
def add():
    task_content = request.form['content'] # Obtenemos el contenido de la tarea del formulario.
    new_task = Task(content=task_content) # Creamos una nueva instancia de la clase Task con el contenido de la tarea.
    db.session.add(new_task) # Agregamos la nueva tarea a la sesión de la base de datos.
    db.session.commit() # Confirmamos los cambios en la base de datos.
    return redirect(url_for('index')) # Redirigimos al usuario a la página de inicio.

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get(id) # Obtenemos la tarea con el ID especificado.
    db.session.delete(task) # Eliminamos la tarea de la base de datos.
    db.session.commit() # Confirmamos los cambios en la base de datos.
    return redirect(url_for('index')) # Redirigimos al usuario a la página de inicio.

if __name__ == '__main__': # Comprobamos si el script se está ejecutando directamente.
    with app.app_context():
        db.create_all() # Creamos todas las tablas en la base de datos.
    app.run(debug=True) # Ejecutamos la aplicación en modo de depuración.







## NOTAS
# Flask es un microframework para Python basado en Werkzeug y Jinja 2, que se utiliza para desarrollar aplicaciones web. Es conocido por su simplicidad y su capacidad para escalar desde pequeñas a grandes aplicaciones.
# SQLAlchemy es una biblioteca de Python que proporciona una forma de interactuar con bases de datos relacionales. SQLAlchemy se utiliza comúnmente en aplicaciones web para interactuar con bases de datos SQL.
# La función principal de Flask en una aplicación web es actuar como el marco de trabajo (framework) que maneja las solicitudes y respuestas HTTP.

# Cuando creas una instancia de la clase Flask, estás creando una nueva aplicación web que espera solicitudes de clientes y sabe cómo responder a ellas.

# Flask proporciona las herramientas necesarias para mapear las URL a funciones de Python, que se conocen como vistas. Estas vistas pueden leer datos de la solicitud, interactuar con una base de datos u otros servicios, y generar una respuesta, que puede ser texto, JSON, una página HTML renderizada, o cualquier otro tipo de contenido que un cliente web pueda manejar.

# Además, Flask también proporciona características para manejar sesiones, cookies, y otras funcionalidades comunes en el desarrollo web.

# Flask y Django son dos frameworks populares para el desarrollo de aplicaciones web en Python, pero tienen diferencias significativas en términos de su filosofía de diseño, características y uso.

# Filosofía de diseño: Flask es un microframework. Esto significa que es ligero, simple y altamente personalizable. Flask viene con muy pocas características incorporadas, lo que te permite elegir las bibliotecas y herramientas que prefieras para cosas como el acceso a la base de datos, la autenticación de usuarios, y más. Esto puede hacer que Flask sea más flexible y más fácil de entender para los nuevos desarrolladores, pero también significa que puedes terminar escribiendo más código y tomando más decisiones sobre cómo hacer las cosas.

# Django, por otro lado, es un framework de "baterías incluidas". Viene con muchas características incorporadas, como un ORM (Object-Relational Mapper), autenticación de usuarios, un sistema de plantillas, y más. Esto puede hacer que Django sea más rápido para desarrollar aplicaciones complejas, ya que muchas funcionalidades comunes ya están incorporadas. Sin embargo, también puede hacer que Django sea más pesado y más difícil de aprender para los nuevos desarrolladores.

# Características: Como se mencionó anteriormente, Django viene con muchas más características incorporadas que Flask. Django incluye su propio ORM, un sistema de plantillas, autenticación de usuarios, un panel de administración automático, y más. Flask, por otro lado, viene con muy pocas características incorporadas, pero hay muchas extensiones disponibles que puedes agregar según sea necesario.

# Uso: Flask es a menudo una buena elección para aplicaciones más pequeñas, proyectos de aprendizaje, o cuando necesitas una gran cantidad de personalización y control. Django puede ser una mejor elección para aplicaciones más grandes y complejas, o cuando quieres que muchas funcionalidades comunes estén ya incorporadas.

# En resumen, la elección entre Flask y Django a menudo se reduce a una cuestión de preferencias personales, el tamaño y la complejidad de tu proyecto, y las características específicas que necesitas.
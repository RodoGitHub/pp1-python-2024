import requests

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/vehiculos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import Marca,Tipo,Vehiculo

#listado_nombres = ['Ana', 'Juan','Jose']

listado_personas = []

"""listado_personas = [
    dict(
        name = dict(
            first='Juan Pablo',
            last='Varsky'
        ),
        location = dict(
            city='Los Angeles'
        ),
        email = 'jpv@gmail.com'
    ),

    dict(
        name = dict(
            first='Rodolfo',
            last='Palacios'
        ),
        location = dict(
            city='Rio Cuarto'
        ),
        email = 'rodo@gmail.com'
    ),

]"""

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/bandas")
def bandas():
    return render_template('bandas.html')

@app.route("/exponentes")
def exponentes():
    return render_template('exponentes.html')

@app.route("/personas")
def personas():
    #peticion = requests.get(url="https://randomuser.me/api/?results=20")
    #respuesta = peticion.json()
    #lista_personas = respuesta['results'] # respuesta.GET.("result")
    listado = listado_personas
    return render_template(
        'personas.html',
        listado = listado
    #   listado=lista_personas
        
    )

@app.route('/personas_add', methods=['POST', 'GET'])
def agregar_personas():
    if request.method == 'POST':
        first_name = request.form['nombre']
        last_Name = request.form['apellido']
        email = request.form['email']
        city = request.form['ciudad']
        
        persona = dict(
            name = dict(
                first = first_name,
                last = last_Name
            ),
            location = dict(
                city = city
            ),
            email = email
            
        )        
        listado_personas.append(persona)

    return render_template ('add_personas.html')
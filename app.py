from flask import Flask
from src.routes.clientes import clientes
from src.routes.veiculos import veiculos

app = Flask(__name__)
app.register_blueprint(clientes)
app.register_blueprint(veiculos)

import os
from flask import Flask
from flask_cors import CORS
from admin import setup_admin

app = Flask(__name__)
CORS(app)

setup_admin(app)

# Si vas a definir rutas, agrégalas aquí
@app.route("/")
def hello():
    return "API funcionando correctamente."

if __name__ == "__main__":
    app.run()

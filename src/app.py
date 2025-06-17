from flask import Flask
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starwars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importar modelos después de definir db
from models import User, Character, Planet, Favorite

# Crear tablas
with app.app_context():
    db.create_all()

# Admin panel
admin = Admin(app, name='StarWars Admin', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Character, db.session))
admin.add_view(ModelView(Planet, db.session))
admin.add_view(ModelView(Favorite, db.session))

# Correr app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)

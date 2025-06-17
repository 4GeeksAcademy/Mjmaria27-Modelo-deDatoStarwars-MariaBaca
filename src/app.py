from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Inicializa la app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starwars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la base de datos
db = SQLAlchemy(app)

# Importa modelos (después de definir `db`)
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    favorites = db.relationship("Favorite", back_populates="user")

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(20))
    birth_year = db.Column(db.String(20))
    eye_color = db.Column(db.String(20))
    favorites = db.relationship("Favorite", back_populates="character")

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(80))
    population = db.Column(db.String(80))
    terrain = db.Column(db.String(80))
    favorites = db.relationship("Favorite", back_populates="planet")

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    user = db.relationship("User", back_populates="favorites")
    character = db.relationship("Character", back_populates="favorites")
    planet = db.relationship("Planet", back_populates="favorites")

# Crea las tablas
with app.app_context():
    db.create_all()

# Configura el panel de administración
admin = Admin(app, name='StarWars Admin', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Character, db.session))
admin.add_view(ModelView(Planet, db.session))
admin.add_view(ModelView(Favorite, db.session))

# Ejecuta la aplicación en el puerto 3000 (compatible con GitHub Codespaces)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)

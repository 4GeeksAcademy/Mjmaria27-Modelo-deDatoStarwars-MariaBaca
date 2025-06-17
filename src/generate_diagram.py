from sqlalchemy import create_engine
from models import db, User, Character, Planet, Favorite
from eralchemy2 import render_er
from flask import Flask

# Crear app temporal solo para generar el diagrama
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    render_er(db.Model, 'diagram.png')

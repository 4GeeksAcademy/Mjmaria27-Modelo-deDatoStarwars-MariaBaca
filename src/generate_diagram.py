from sqlalchemy import create_engine
from models import Base
from eralchemy2 import render_er

# Crear DB en memoria
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Generar el diagrama
render_er(Base, 'diagram.png')

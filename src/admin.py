import os
from flask_admin import Admin
from models import User, Character, Planet, Favorite
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    from models import Base
    from sqlalchemy.orm import scoped_session, sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine(os.getenv('DATABASE_URL'))
    Base.metadata.bind = engine
    db_session = scoped_session(sessionmaker(bind=engine))

    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db_session))
    admin.add_view(ModelView(Character, db_session))
    admin.add_view(ModelView(Planet, db_session))
    admin.add_view(ModelView(Favorite, db_session))

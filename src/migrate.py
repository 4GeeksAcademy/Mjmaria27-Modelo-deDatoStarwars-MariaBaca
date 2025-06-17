import os
from sqlalchemy import create_engine
from models import Base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///test.db")

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

print("✅ Tablas creadas correctamente.")

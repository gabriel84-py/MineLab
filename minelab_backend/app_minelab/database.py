# minelab_backend/app_minelab/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///minelab_backend/minelab.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # pour SQLite
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# pour FastAPI : fournir une session par requête
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

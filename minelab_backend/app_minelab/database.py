import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(BASE_DIR, "minelab_backend")
os.makedirs(DB_DIR, exist_ok=True)  # <-- crée le dossier s'il n'existe pas

DATABASE_URL = f"sqlite:///{os.path.join(DB_DIR, 'minelab.db')}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

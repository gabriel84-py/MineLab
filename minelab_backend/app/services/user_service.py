from models.user import User
from app.database import Base, engine, SessionLocal

def create_user(email: str, passwd: str):

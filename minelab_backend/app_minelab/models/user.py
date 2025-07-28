from sqlalchemy import Column, Integer, String
from minelab_backend.app_minelab.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

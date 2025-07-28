from sqlalchemy import Column, Integer, String
from app.database import Base

class Plugin(Base):
    __tablename__ = "plugins"

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String, unique=True, index=True)
    expiration_date = Column(String)

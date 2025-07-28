from sqlalchemy import Column, Integer, String
from minelab_backend.app_minelab.database import Base

class License(Base):
    __tablename__ = "license"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

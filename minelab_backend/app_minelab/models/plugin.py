from sqlalchemy import Column, Integer, String, Date
from minelab_backend.app_minelab.database import Base

class Plugin(Base):
    __tablename__ = "plugins"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    owner = Column(Integer, unique=True, index=True)
    nb_de_hash = Column(Integer)
    expiration_date = Column(Date)

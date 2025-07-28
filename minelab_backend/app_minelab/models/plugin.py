from sqlalchemy import Column, Integer, String
from minelab_backend.app_minelab.database import Base
class Plugin(Base):
    __tablename__ = "plugins"

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String, unique=True, index=True)
    expiration_date = Column(String)

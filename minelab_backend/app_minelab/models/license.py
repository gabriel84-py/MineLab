from sqlalchemy import Column, Integer, String, JSON
from minelab_backend.app_minelab.database import Base

class License(Base):
    __tablename__ = "license"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hash = Column(JSON, unique=True, index=True, nullable=False, default=0)
    size = Column(Integer)
    activate_times = Column(Integer)
    owner_id = Column(Integer)
    activations_autorisees = Column(Integer, server_default="0")
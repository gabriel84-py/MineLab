from sqlalchemy import Column, Integer, String
from minelab_backend.app_minelab.database import Base

class License(Base):
    __tablename__ = "license"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hash = Column(String, unique=True, index=True, nullable=False)
    size = Column(Integer)
    activate_times = Column(Integer)
    owner_id = Column(Integer)

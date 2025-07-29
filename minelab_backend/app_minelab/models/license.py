from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from minelab_backend.app_minelab.database import Base

class License(Base):
    __tablename__ = "license"

    id = Column(Integer, primary_key=True, index=True)
    size = Column(Integer)
    activate_times = Column(Integer)
    owner_id = Column(Integer)
    activations_autorisees = Column(Integer, server_default="0")

    hashes = relationship("LicenseHash", back_populates="license")  # relation vers LicenseHash


class LicenseHash(Base):
    __tablename__ = "license_hash"

    id = Column(Integer, primary_key=True, index=True)
    hash = Column(String, unique=True, nullable=False)
    license_id = Column(Integer, ForeignKey("license.id"))

    license = relationship("License", back_populates="hashes")

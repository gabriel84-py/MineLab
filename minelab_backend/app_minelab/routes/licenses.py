from fastapi import APIRouter
from minelab_backend.app_minelab.services.license_checker import license_checker
from minelab_backend.app_minelab.services.add_licence import  add_license
from minelab_backend.app_minelab.services.add_hash_license import  add_hash
from minelab_backend.app_minelab.services.signer_json import signer_json
from minelab_backend.app_minelab.database import Base, engine, SessionLocal
from minelab_backend.app_minelab.models.license import License, LicenseHash
from minelab_backend.app_minelab.models.plugin import Plugin

router = APIRouter(prefix="/verify", tags=["Verify"])

@router.get("")
def verify(id: int, hash: str, taille: int):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    is_existing_licence = db.query(License).filter_by(id=id).first()
    id_plugin = db.query(Plugin).filter_by(id=id).first()
    if not is_existing_licence and id_plugin:
        add_license(hash, taille, id_plugin.owner, id_plugin.nb_de_hash)
        return {"status": "valid", "message": "Licence active."}

    if hash != is_existing_licence.hashes:
        add_hash(is_existing_licence.id, taille, hash)

    if license_checker(id, hash, taille):
        return { "status": "valid", "message": "Licence active." }
    else:
        return { "status": "invalid", "message": "Licence not active." }
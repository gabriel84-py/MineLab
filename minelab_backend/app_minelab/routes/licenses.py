from fastapi import APIRouter
from minelab_backend.app_minelab.services.license_checker import license_checker
from minelab_backend.app_minelab.services.add_licence import  add_license
from minelab_backend.app_minelab.services.signer_json import signer_json

router = APIRouter(prefix="/verify", tags=["Verify"])

@router.get("")
def verify(id: int, hash: str, taille: int):
    if license_checker(id, hash, taille):
        return { "status": "valid", "message": "Licence active." }
    else:
        return { "status": "invalid", "message": "Licence not active." }
from fastapi import APIRouter
from minelab_backend.app_minelab.services.auth_user import auth_user
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/", response_class=HTMLResponse)
def auth(email: str, password: str):
    if auth_user(email, password):
        return "<h1> vous ici ! </h1>"
    else:
        return "<h1> vas te faire foutre </h1>"

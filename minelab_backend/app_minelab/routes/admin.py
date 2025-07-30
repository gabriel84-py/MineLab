from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.resources import Model
from fastapi_admin.widgets import displays, inputs
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI
from minelab_backend.app_minelab.models.user import User
from minelab_backend.app_minelab.database import Base, engine, SessionLocal
from minelab_backend.app_minelab.models.license import License, LicenseHash
from minelab_backend.app_minelab.models.plugin import Plugin
from minelab_backend.app_minelab.models.user import User

class AdminUser:
    def __init__(self, id: int):
        self.id = id
        self.username = "admin"

    def get_display_name(self) -> str:
        return self.username

provider = UsernamePasswordProvider(
    admin_model=None,
    login_logo_url="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png",
    authenticate=lambda request, username, password: AdminUser(1) if username == "admin" and password == "admin" else None
)

async def setup_admin(app: FastAPI):
    app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

    await admin_app.init(
        admin_secret="admin",
        engine=engine,
        providers=[provider],
    )

    class UserAdmin(Model):
        label = "Users"
        model = User
        icon = "fas fa-user"
        fields = [
            "id",
            "email",
            "hashed_password"
        ]
        page_size = 20

    admin_app.register(UserAdmin)
    app.mount("/admin", admin_app)
from fastapi import FastAPI
from minelab_backend.app_minelab.routes import auth, licenses, admin
#from minelab_backend.app_minelab.routes.auth import admin import setup_admin
from minelab_backend.app_minelab.database import engine, Base

app = FastAPI()

app.include_router(auth.router)
app.include_router(licenses.router)

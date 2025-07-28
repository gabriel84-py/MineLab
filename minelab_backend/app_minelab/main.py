from fastapi import FastAPI
from minelab_backend.app_minelab.routes import auth, licenses

app = FastAPI()

app.include_router(auth.router)

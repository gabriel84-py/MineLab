from minelab_backend.app_minelab.database import Base, engine, SessionLocal
from minelab_backend.app_minelab.models.plugin import Plugin
from datetime import date

Base.metadata.create_all(bind=engine)

def add_plugin(owner_id: int, nb_activations: int, expiration_date: date):
    with SessionLocal() as db:
        new_plugin = License(
            owner=owner_id,
            nb_de_hash=nb_activations,
            expiration_date=expiration_date
        )
        db.add(new_plugin)
        db.commit()
        db.refresh(new_plugin)
        print("Plugin ajouté :", new_plugin.id)
        return new_plugin
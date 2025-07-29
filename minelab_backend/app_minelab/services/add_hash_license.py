from minelab_backend.app_minelab.database import Base, engine, SessionLocal
from minelab_backend.app_minelab.models.license import License

def add_hash(id_sent: int, taille_sent: int, hash_sent: str):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    existing_licence = db.query(License).filter_by(id=id_sent).first()

    if existing_licence and existing_licence.activate_times < existing_licence.activations_autorisées and taille_sent == existing_licence.size:
        existing_licence.hash.append(hash_sent)

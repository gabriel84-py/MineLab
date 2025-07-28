from minelab_backend.app_minelab.database import Base, engine, SessionLocal
from minelab_backend.app_minelab.models.license import License

def license_checker(id_sent: int, hash_sent: str, taille: int):
    # Crée la BDD si elle n'existe pas
    Base.metadata.create_all(bind=engine)

    # Crée une session locale
    db = SessionLocal()

    existing_license = db.query(License).filter_by(id=id_sent).first()

    if existing_license.hash == hash_sent and existing_license.size == taille:
        return True
    else:
        return False

if __name__ == "__main__":
    print(license_checker(3, "hello", 1))
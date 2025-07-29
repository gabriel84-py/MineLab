from minelab_backend.app_minelab.database import Base, engine, SessionLocal
from minelab_backend.app_minelab.models.license import License

def license_checker(id_sent: int, hash_sent: str, taille: int):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        existing_license = db.query(License).filter_by(id=id_sent).first()
        if not existing_license:
            return False

        # Vérifier la taille
        if existing_license.size != taille:
            return False

        # Vérifier si le hash existe parmi les hashes liés
        for license_hash in existing_license.hashes:
            if license_hash.hash == hash_sent:
                return True

        return False
    finally:
        db.close()


if __name__ == "__main__":
    print(license_checker(1, "hello", 1))

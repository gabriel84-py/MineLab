from minelab_backend.app_minelab.database import Base, engine, SessionLocal
from minelab_backend.app_minelab.models.license import License


def add_license(hash_sent: str, size: int, owner_id: int):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    new_license = License(hash=hash_sent, size=size, owner_id=owner_id)
    existing_licence = db.query(License).filter_by(hash=hash_sent).first()

    if existing_licence:
        print("License déjà existante :", existing_licence)
        return existing_licence
    else:
        db.add(new_license)
        db.commit()
        db.refresh(new_license)  # <= seulement ici, après ajout réussi
        print("License ajouté :", new_license)
        return new_license

if __name__ == "__main__":
    helo = add_license("hello", 1, 1)
    print(helo.id)
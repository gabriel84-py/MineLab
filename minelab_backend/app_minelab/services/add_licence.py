from minelab_backend.app_minelab.database import Base, engine, SessionLocal
from minelab_backend.app_minelab.models.license import License, LicenseHash

Base.metadata.create_all(bind=engine)


def add_license(hash_sent: str, size: int, owner_id: int, nb_de_hash: int):
    with SessionLocal() as db:
        # Vérifie si le hash existe déjà
        existing_hash = db.query(LicenseHash).filter_by(hash=hash_sent).first()
        if existing_hash:
            print("Hash déjà associé à une licence :", existing_hash.license_id)
            return existing_hash.license

        # Crée une nouvelle licence
        new_license = License(
            size=size,
            owner_id=owner_id,
            activations_autorisees=nb_de_hash,
            activate_times=1

        )

        # Ajoute le hash comme objet lié
        new_hash = LicenseHash(hash=hash_sent)
        new_license.hashes.append(new_hash)

        db.add(new_license)
        db.commit()
        db.refresh(new_license)

        print("Licence ajoutée :", new_license.id)
        return new_license


if __name__ == "__main__":
    license = add_license("hello", 1, 1, 3)
    print("ID de la licence :", license.id)

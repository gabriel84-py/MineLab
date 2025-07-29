from minelab_backend.app_minelab.database import Base, engine, SessionLocal
from minelab_backend.app_minelab.models.license import License, LicenseHash

def add_hash(id_sent: int, taille_sent: int, hash_sent: str):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        existing_licence = db.query(License).filter_by(id=id_sent).first()

        if existing_licence is None:
            print("Licence introuvable.")
            return

        if existing_licence.activate_times >= existing_licence.activations_autorisees:
            print("Limite d'activations atteinte.")
            return

        if existing_licence.size != taille_sent:
            print("Taille invalide.")
            return

        # Vérifie si le hash est déjà utilisé globalement
        existing_hash = db.query(LicenseHash).filter_by(hash=hash_sent).first()
        if existing_hash:
            print("Ce hash est déjà associé à une licence.")
            return

        # Création du nouveau hash lié à la licence
        new_hash = LicenseHash(hash=hash_sent, license_id=existing_licence.id)
        db.add(new_hash)

        # Incrémente le compteur d’activations
        existing_licence.activate_times += 1

        db.commit()
        db.refresh(existing_licence)

        print("Hash ajouté :", hash_sent)
        print("Activate_times mis à jour :", existing_licence.activate_times)

    finally:
        db.close()


if __name__ == "__main__":
    add_hash(1, 1, "hellilr")
from minelab_backend.app_minelab.database import Base, engine, SessionLocal
from minelab_backend.app_minelab.models.license import License

def changer_taille(id_sent: int, taille_sent: int):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    license_obj = db.query(License).filter(License.id == id_sent).first()

    # Étape 3 : Vérifier si elle existe
    if license_obj:
        # Étape 4 : Modifier la valeur de size
        license_obj.size = taille_sent  # ← nouvelle valeur
        db.commit()
        db.refresh(license_obj)
        print("Taille mise à jour :", license_obj.size)
    else:
        print("Licence non trouvée")

    db.close()


if __name__ == "__main__":
    changer_taille(6, 60419744)
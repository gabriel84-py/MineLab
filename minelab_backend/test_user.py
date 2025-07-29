from app_minelab.models.license import License
from app_minelab.database import Base, engine, SessionLocal

# Crée la BDD si elle n'existe pas
Base.metadata.create_all(bind=engine)

# Crée une session locale
db = SessionLocal()

existing_user = db.query(License).filter_by(id=1).first()

# Affiche l'id généré automatiquement
print(existing_user.hashes)

# Ferme la session proprement
db.close()

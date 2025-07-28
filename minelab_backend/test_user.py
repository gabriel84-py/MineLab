from app_minelab.models.user import User
from app_minelab.database import Base, engine, SessionLocal

# Crée la BDD si elle n'existe pas
Base.metadata.create_all(bind=engine)

# Crée une session locale
db = SessionLocal()

# Crée un nouvel utilisateur
new_user = User(email="alice@example.com", hashed_password="...")

existing_user = db.query(User).filter_by(email="alice@example.com").first()

if existing_user:
    print("Utilisateur déjà existant :", existing_user)
else:
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # <= seulement ici, après ajout réussi
    print("Utilisateur ajouté :", new_user)


# Affiche l'id généré automatiquement
print(existing_user.id)

# Ferme la session proprement
db.close()

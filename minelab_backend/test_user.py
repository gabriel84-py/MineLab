from app.models.user import User
from app.database import Base, engine, SessionLocal

# Crée la BDD si elle n'existe pas
Base.metadata.create_all(bind=engine)

# Crée une session locale
db = SessionLocal()

# Crée un nouvel utilisateur
new_user = User(email="alice@example.com", hashed_password="...")

# Ajoute et commit dans la session
db.add(new_user)
db.commit()

# Recharge l'objet pour que l'id soit mis à jour
db.refresh(new_user)

# Affiche l'id généré automatiquement
print(new_user.id)

# Ferme la session proprement
db.close()

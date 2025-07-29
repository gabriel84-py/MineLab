from minelab_backend.app_minelab.database import Base, engine, SessionLocal
from minelab_backend.app_minelab.models.license import License

id_sent = int(input("ID de la license : "))

Base.metadata.create_all(bind=engine)
db = SessionLocal()

existing_licence = db.query(License).filter_by(id=id_sent).first()

print(existing_licence.hash)
from app.models import User
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

print(User.__tablename__)

from minelab_backend.app_minelab.models.user import User
from minelab_backend.app_minelab.database import Base, engine, SessionLocal
import hashlib


def auth_user(email: str, passwd_sent: str):
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    existing_user = db.query(User).filter_by(email=email).first()

    if existing_user:
        passwd = bytes(passwd_sent, "utf-8")
        hash_one = hashlib.sha512(passwd).hexdigest()
        if existing_user.hashed_password == hash_one:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    print(auth_user("hello@hello.com", "je suis trop nuuuul"))
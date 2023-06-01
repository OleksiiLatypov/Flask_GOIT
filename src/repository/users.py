from src import db, models
import bcrypt

from src.models import User


def create_user(email, password, nick):
    hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=10))
    user = models.User(username=nick, email=email, hash=hash)
    db.session.add(user)
    db.session.commit()
    return user


def login(email, password):
    user = find_by_email(email)
    if not user:
        return None
    if not bcrypt.checkpw(password.encode('user-8'), user.hash):
        return None
    return user


def find_by_email(email):
    email = db.session.query(User).filter(User.email == email).first()
    return email

from sqlalchemy.orm import Session

from ..models.users import User
from ..schemas.users import UserDB


def greeting(user_for_greeting: User, database: Session):
    user = database.query(UserDB).filter(UserDB.email == user_for_greeting.email).first()
    if not user:
        user = UserDB(email=user_for_greeting.email)
        database.add(user)
        database.commit()
        database.refresh(user)
        return f"Hello, {user_for_greeting.email}"
    else:
        return f"We have already met, {user_for_greeting.email}"


def view_all(database: Session):
    emails = [user_emails.email for user_emails in database.query(UserDB.email).all()]
    return emails

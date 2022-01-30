from sqlalchemy import Column, Integer, Text

from ..database.database_init import Base


class UserDB(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(Text, unique=True, nullable=False)

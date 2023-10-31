from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean
from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    nickname = Column(String)


class Charges(Base):
    __tablename__ = "charges"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, unique=True, nullable=False)

class Members(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, unique=True, nullable=False)
    blood_type = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    image = Column(String)
    birthdate = Date
    is_active = Boolean
    register_date = DateTime

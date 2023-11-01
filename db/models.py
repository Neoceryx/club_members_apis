from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
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
    members = relationship("members", backref="charges", cascade="delete, merge") # foreign key

class Members(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    charges_id = Column(Integer, ForeignKey("charges.id", ondelete="CASCADE")) # Foreign Key
    fullname = Column(String, unique=True, nullable=False)
    blood_type = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    image = Column(String)
    birthdate = Column(DateTime)
    is_active = Column(Boolean)
    register_date = Column(DateTime)

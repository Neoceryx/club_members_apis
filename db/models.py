import datetime

from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class Bikes(Base):
    __tablename__ = "bikes"

    id = Column(Integer, primary_key=True, index=True)
    members_id = Column(Integer, ForeignKey("members.id", ondelete="CASCADE"), nullable=False)
    plate_number = Column(String, nullable=False)
    register_date = Column(DateTime, default=datetime.datetime.now())


class Emergency_Contacts(Base):
    __tablename__ ="emergency_contacts"

    id = Column(Integer, primary_key=True, index=True)
    members_id = Column(Integer, ForeignKey("members.id", ondelete="CASCADE"), nullable=False)  # Foreign Keys
    fullname = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    relationship = Column(String, nullable=False)
    register_date = Column(DateTime, default=datetime.datetime.now())

class Charges(Base):
    __tablename__ = "charges"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, unique=True, nullable=False)
    members = relationship("Members", backref="charges", cascade="delete, merge") # foreign key


class Members(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    charges_id = Column(Integer, ForeignKey("charges.id", ondelete="CASCADE"), nullable=False)  # Foreign Key
    fullname = Column(String, unique=True, nullable=False)
    blood_type = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    image = Column(String)
    birthdate = Column(DateTime)
    is_active = Column(Boolean)
    register_date = Column(DateTime, default=datetime.datetime.now())

    emergency_contacts = relationship("Emergency_Contacts", backref="members", cascade="delete, merge")
    bikes = relationship("Bikes", backref="members", cascade="delete, merge")

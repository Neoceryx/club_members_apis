from datetime import datetime

from sqlalchemy.orm import Session
from db.models import Members
from schemas.member_sh import member_schema


# This class contains All the Operation related with the Data Base
class members_Dal:

    def get_all(self, db: Session):
        return db.query(Members).all()

    def is_fullname_duplicated(self, fullname: str, db: Session):
        return db.query(Members).filter(Members.fullname == fullname).count()

    def is_email_registered(self, email: str, db: Session):
        return db.query(Members).filter(Members.email == email).count()

    def new_member(self, new_member: member_schema, db: Session):

        member = Members()

        member.charges_id = new_member.charges_id
        member.fullname = new_member.fullname
        member.blood_type = new_member.blood_type
        member.email = new_member.email
        member.password = new_member.password
        member.address = new_member.address
        member.phone_number = new_member.phone_number
        member.image = new_member.image
        member.birthdate = new_member.birthdate
        member.is_active = new_member.is_active
        member.register_date = datetime.now()

        # save it on DB
        db.add(member)
        db.commit()
        db.refresh(member)

        # return the new member id registered
        return member.id

    def get_by_email_and_password(self, email, password, db: Session):
        return db.query(Members).filter(Members.email == email, Members.password == password).first()
        pass

    pass
    # end class

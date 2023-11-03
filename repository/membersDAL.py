from sqlalchemy.orm import Session
from db.models import Members


# This class contains All the Operation related with the Data Base


class members_Dal:

    def get_all(self, db: Session):
        return db.query(Members).all()

    def is_fullname_duplicated(self, fullname: str, db: Session):
        return db.query(Members).filter(Members.fullname == fullname).count()

    def is_email_registered(self, email: str, db: Session):
        return db.query(Members).filter(Members.email == email).count()

    pass
    # end class

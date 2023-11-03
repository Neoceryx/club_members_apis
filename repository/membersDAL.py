from sqlalchemy.orm import Session
from db.models import Members


# This class contains All the Operation related with the Data Base


class members_Dal:

    def get_all(self, db: Session):
        member_list = db.query(Members).all()
        return member_list
        # end method

    # end class

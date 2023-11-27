from sqlalchemy.orm import Session
from db.models import Charges

class charge_DAL:

    def get_all(self, db: Session):
        return db.query(Charges).all()

    pass
    # end class
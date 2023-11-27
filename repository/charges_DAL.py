from sqlalchemy.orm import Session
from db.models import Charges
from schemas.charges import charge_schema


class charge_DAL:

    def get_all(self, db: Session):
        return db.query(Charges).all()

    def save_new_charge(self, new_charge: charge_schema, db: Session):
        charge = Charges()  # create Entity Object

        charge.description = new_charge.description

        # save it on BD
        db.add(charge)
        db.commit()
        db.refresh(charge)

        return charge.id  # it will return the new charge saved ID

    pass
    # end class

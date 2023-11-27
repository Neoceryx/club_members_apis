from sqlalchemy.orm import Session
from repository.charges_DAL import charge_DAL
from schemas.charges import charge_schema

class charge_BLL:
    charge_DAL = None

    # Class constructor
    def __init__(self):
        self.charge_DAL = charge_DAL()

    def get_charges(self, db: Session):
        return self.charge_DAL.get_all(db)

    def new_charge(self, new_charge: charge_schema, db: Session):
        # TODO: Create a common class, with the method to return a correct format for strings, in Camel Case
        new_charge.description = new_charge.description.title()







    pass
    # end charge_BLL class

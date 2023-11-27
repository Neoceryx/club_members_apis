from sqlalchemy.orm import Session
from repository.charges_DAL import charge_DAL
class charge_BLL:

    charge_DAL = None

    # Class constructor
    def __init__(self):
        self.charge_DAL = charge_DAL()

    def get_charges(self, db: Session):
        return self.charge_DAL.get_all(db)

    pass
    # end charge_BLL class
from sqlalchemy.orm import Session
from repository.membersDAL import members_Dal

# This class will contain all the Business logic
class members_Bll:


    members_Dal: members_Dal = None

    def __init__(self):
        self.members_Dal = members_Dal()

    def get_all_members(self, db: Session):
        return self.members_Dal.get_all(db)

    pass
    # end class

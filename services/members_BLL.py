from sqlalchemy.orm import Session
from repository.membersDAL import members_Dal
from schemas.member_sh import member_schema

# This class will contain all the Business logic
class members_Bll:


    members_Dal: members_Dal = None

    def __init__(self):
        self.members_Dal = members_Dal()

    def get_all_members(self, db: Session):
        return self.members_Dal.get_all(db)


    def new_member(self, new_member:member_schema, db:Session):

        is_fullname_registered = self.members_Dal.is_fullname_duplicated(new_member.fullname, db)
        print(is_fullname_registered)

        # validate member name is not duplicated
        # validate email is not duplicated

        pass

    pass
    # end class

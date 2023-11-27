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

    def new_member(self, new_member: member_schema, db: Session):

        is_fullname_registered = self.members_Dal.is_fullname_duplicated(new_member.fullname, db)
        is_email_registered = self.members_Dal.is_email_registered(new_member.email, db)

        # As Member is OK
        response = 0

        # Verify member name and email is not duplicated by other member
        if is_fullname_registered == 0:
            if is_email_registered == 0:

                # register new member and retrieve him id
                response = self.members_Dal.new_member(new_member, db)

            else:
                response = -2  # email is already registered
        else:
            response = -1  # member name is already registered

        return response

    def get_by_email_and_password(self, email, password, db: Session):
        user = self.members_Dal.get_by_email_and_password(email, password, db)
        return user

    pass
    # end class

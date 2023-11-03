from fastapi import APIRouter, Depends
import datetime

from schemas.member_sh import member_schema
from db.models import Members
from db.database import get_db
from sqlalchemy.orm import Session
from services.members_BLL import members_Bll

member_rute = APIRouter(
    prefix="/members",
    tags=["members"]
)

members_bll = members_Bll()

@member_rute.get("/")
async def get_all(db: Session = Depends(get_db)):
    member_list = members_bll.get_all_members(db)
    return member_list


@member_rute.post("/")
async def create_new(new_member: member_schema, db: Session = Depends(get_db)):

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
    member.register_date = datetime.datetime.now()

    # save it on DB
    # db.add(member)
    # db.commit()
    # db.refresh(member)

    return {"response": "helo"}

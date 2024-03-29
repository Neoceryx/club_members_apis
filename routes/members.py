﻿from fastapi import APIRouter, Depends
from schemas.member_sh import member_schema
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
    result = members_bll.new_member(new_member, db)

    response = dict()

    # Build response
    if result > 0:
        response = {"message": "New member has been created"}
    elif result == -1:
        response = {"message": "This member is already registered"}
    elif result == -2:
        response = {"message": "This email is already registered"}

    return response

# TODO:  perform inner join with 'charges' table to get the charge name also.
@member_rute.post("/login")
async def get_by_email_and_password(email: str, password: str, db: Session = Depends(get_db)):
    return members_bll.get_by_email_and_password(email, password, db)

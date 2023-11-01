from fastapi import APIRouter, Depends

from schemas.member_sh import member_schema
from db.models import Members
from db.database import get_db
from sqlalchemy.orm import Session

member_rute = APIRouter(
    prefix="/members",
    tags=["members"]
)


@member_rute.get("/")
async def get_all(db: Session = Depends(get_db)):
    member_list = db.query(Members).all()
    return member_list


@member_rute.post("/")
async def get_by_id_and_password(new_member: member_schema, db: Session = Depends(get_db)):
    return {"response": "helo"}

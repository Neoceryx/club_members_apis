from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from services.charges_BLL import charge_BLL
from schemas.charges import charge_schema

charge_rute = APIRouter(
    prefix="/charges",
    tags=["charges"]
)

charge_bll = charge_BLL()


@charge_rute.get("/")
async def get_charges(db: Session = Depends(get_db)):
    return charge_bll.get_charges(db)


@charge_rute.post("/")
async def create_newone(new_charge: charge_schema, db: Session = Depends(get_db)):
    return charge_bll.new_charge(new_charge, db)

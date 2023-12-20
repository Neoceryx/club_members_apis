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

# TODO: Write unit test for this api. to confirm correct functionality
@charge_rute.post("/")
async def create_newone(new_charge: charge_schema, db: Session = Depends(get_db)):
    response_code = charge_bll.new_charge(new_charge, db)

    # Build API response
    response = dict()

    if response_code > 0:
        response = {"message": "New charge was beed created"}
    elif response_code == -1:
        response = {"message": "This Charge is already registered, please write a different description"}

    return response

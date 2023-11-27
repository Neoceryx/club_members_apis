from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from services.charges_BLL import charge_BLL

charge_rute = APIRouter(
    prefix="/charges",
    tags=["charges"]
)

charge_bll = charge_BLL()

@charge_rute.get("/")
async def get_charges(db: Session = Depends(get_db)):
    return charge_bll.get_charges(db)


from fastapi import APIRouter, Depends

from db.database import get_db
from sqlalchemy.orm import Session

charge_rute = APIRouter(
    prefix="/charges",
    tags=["charges"]
)


@charge_rute.get("/")
async def get_charges():
    return {"msg": "Charge rute say HI"}
    pass

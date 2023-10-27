from fastapi import APIRouter

# schemas
from schemas.member_sh import member_schema

member_rute = APIRouter(
    prefix="/members",
    tags=["members"]
)


@member_rute.get("/")
async def get_all():
    return {"response": "Getting all members"}


@member_rute.post("/")
async def get_by_id_and_password(member: member_schema):
    return {"response": "helo"}

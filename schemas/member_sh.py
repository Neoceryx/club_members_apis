from pydantic import BaseModel


class member_schema(BaseModel):
    id: int
    name: str
    email: str
    nickname: str

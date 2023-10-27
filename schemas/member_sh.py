from pydantic import BaseModel


class member_schema(BaseModel):
    username: str
    password: str

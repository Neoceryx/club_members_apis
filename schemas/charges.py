from pydantic import BaseModel


class charge_schema(BaseModel):
    description: str
    
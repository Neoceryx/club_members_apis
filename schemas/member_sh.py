from pydantic import BaseModel


class member_schema(BaseModel):
    charges_id: int
    fullname: str
    blood_type: str
    email: str
    password: str
    address: str
    phone_number: str
    image: str
    birthdate: str
    is_active: bool

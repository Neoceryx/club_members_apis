from pydantic import BaseModel


class member_schema(BaseModel):
    id = int
    charges_id = int
    fullname = str
    blood_type = str
    email = str
    password = str
    address = str
    phone_number = str
    image = str
    birthdate = str
    is_active = str
    register_date = str

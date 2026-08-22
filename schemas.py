from pydantic import BaseModel


class UserBase(BaseModel):
    full_name: str
    last_name: str
    role: str
    email: str
    password: str
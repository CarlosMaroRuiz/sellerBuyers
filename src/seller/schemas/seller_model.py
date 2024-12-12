from pydantic import BaseModel, EmailStr

class Seller(BaseModel):
    username: str
    email: EmailStr
    password: str
    idRol: int = 2

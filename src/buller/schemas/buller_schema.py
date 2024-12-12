from pydantic import BaseModel, EmailStr

class Buyer(BaseModel):
    username: str
    email: EmailStr
    password: str
    idRol: int = 1

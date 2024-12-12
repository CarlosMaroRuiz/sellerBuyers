from pydantic import BaseModel, EmailStr

class Seller_Login(BaseModel):
    email: EmailStr
    password: str

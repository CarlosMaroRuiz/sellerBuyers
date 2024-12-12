from pydantic import BaseModel, EmailStr

class BuyerLogin(BaseModel):
    email: EmailStr
    password: str

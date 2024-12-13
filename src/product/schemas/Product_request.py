from pydantic import BaseModel, Field

class Product_request(BaseModel):
    name: str
    quantity: int

    class Config:
        orm_mode = True
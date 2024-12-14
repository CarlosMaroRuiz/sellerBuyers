from pydantic import BaseModel, Field

class Product_request(BaseModel):
    productId:int
    quantity: int

    class Config:
        orm_mode = True